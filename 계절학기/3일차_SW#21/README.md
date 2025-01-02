# 유지보수
요청한 시간부터 장 시작 시간까지의 체결가격 정보를 받아오는 코드블럭
## 리팩토링 전
```py
 def get_d_stock_chart_data_day_for_realtime(access_token, stock_code, current_time):
     base_url = settings.KIS_BASE_URL
     path = "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
     url = f"{base_url}{path}"

     headers = {
         "Content-Type": "application/json; charset=utf-8",
         "authorization": f"Bearer {access_token}",
         "appkey": settings.KIS_APP_KEY,
         "appsecret": settings.KIS_APP_SECRET,
         "tr_id": "FHKST03010200"
     }

     # current_time이 153000(장이 마감되는 시간)을 초과하면 153000으로 설정
     if int(current_time) > 153000:
         current_time = "153000"

     # 주말일 경우 금요일 날짜로 설정
     today = datetime.now()
     if today.weekday() >= 5:  # 토요일(5) 또는 일요일(6)
         days_to_friday = today.weekday() - 4
         friday_date = today - timedelta(days=days_to_friday)
         current_date = friday_date.strftime("%Y%m%d")
     else:
         current_date = today.strftime("%Y%m%d")

     # current_time에서 1시간 전 시간 계산 (HHMMSS 형식)
     time_format = "%H%M%S"
     start_time = '090000'
     current_datetime = datetime.strptime(current_time, time_format)
     one_hour_ago = (current_datetime - timedelta(minutes=30)).strftime(time_format)

     if int(one_hour_ago) < 90000:
         one_hour_ago = start_time
         print(type(one_hour_ago))

     params = {
         "FID_ETC_CLS_CODE": "",
         "FID_COND_MRKT_DIV_CODE": "J",
         "FID_INPUT_ISCD": stock_code,
         "FID_INPUT_HOUR_1": current_time,
         "FID_PW_DATA_INCU_YN": "N",
     }

     chart_data = []
     try:
         response = requests.get(url, headers=headers, params=params)
         response.raise_for_status()
         data = response.json()

         if data['rt_cd'] == '0':  # Successful response
             for item in data['output2']:
                 time_value = item['stck_cntg_hour']

                 # Stop if data is outside the requested range
                 if time_value < one_hour_ago:
                     break

                 chart_data.append({
                     'time': time_value,
                     'price': float(item['stck_prpr'])
                 })


         else:  # Handle API error
             raise Exception(f"API Error: {data['msg1']}")
         print(chart_data)
         return chart_data

     except Exception as e:
         print(f"Error getting price for stock {stock_code}: {str(e)}")
         return []
```

## 리팩토링 후 
```py
def get_d_stock_chart_data_day_for_realtime(access_token, stock_code, current_time):
    base_url = settings.KIS_BASE_URL
    path = "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
    url = f"{base_url}{path}"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "authorization": f"Bearer {access_token}",
        "appkey": settings.KIS_APP_KEY,
        "appsecret": settings.KIS_APP_SECRET,
        "tr_id": "FHKST03010200"
    }

    # current_time이 153000(장이 마감되는 시간)을 초과하면 153000으로 설정
    if int(current_time) > 153000:
        current_time = "153000"

    # 주말일 경우 금요일 날짜로 설정
    today = datetime.now()
    if today.weekday() >= 5:  # 토요일(5) 또는 일요일(6)
        days_to_friday = today.weekday() - 4
        friday_date = today - timedelta(days=days_to_friday)
        current_date = friday_date.strftime("%Y%m%d")
    else:
        current_date = today.strftime("%Y%m%d")

    # 주식 시장의 시작 시간
    start_time = '090000'
    
    # chart_data 초기화
    chart_data = []

    # 반복적으로 데이터를 요청하며 chart_data에 추가
    while int(current_time) >= int(start_time):
        params = {
            "FID_ETC_CLS_CODE": "",
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": stock_code,
            "FID_INPUT_HOUR_1": current_time,
            "FID_PW_DATA_INCU_YN": "N",
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if data['rt_cd'] == '0':  
                for item in data['output2']:
                    time_value = item['stck_cntg_hour']
                    price_value = float(item['stck_prpr'])
                    
                    # 중복 데이터 방지: 이미 저장된 시간은 추가하지 않음
                    if not any(d['time'] == time_value for d in chart_data):
                        chart_data.append({
                            'time': time_value,
                            'price': price_value
                        })
            else:  # Handle API error
                raise Exception(f"API Error: {data['msg1']}")
        except Exception as e:
            print(f"Error getting price for stock {stock_code}: {str(e)}")
            return []

        # 30분 전으로 시간 감소
        current_datetime = datetime.strptime(current_time, "%H%M%S") - timedelta(minutes=30)
        current_time = current_datetime.strftime('%H%M%S')

        # 장 시작 시간 이전으로 가면 종료
        if int(current_time) < int(start_time):
            break

    return chart_data
```


## 개선사항
1. 성능개선: 기존 코드 대비 80% 향상된 속도
2. 직관적인 코드: While을 통해 장 시작시간까지 계속 API를 반복 호출하여 chart_data를 채운 후 반환한다는 점에 대한 직관성 확보