# PJT-04 후기

## 단계별 어려웠던 점

### PROBLEM-1
- django 또는 pandas 또는 matplotlib 내부에 table을 만들 수 있는 기능이 있는 줄 알고 그거 찾느라 시간을 많이 소비함. 물론 있겠지..? 하지만 단순하게 구현하는 방법을 찾지는 못했음
- 가장 단순한 방법으로 html의 talbe 태그를 활용하기로 결정. 이쁘지는 않지만 정보를 표현하는데는 성공.

### PROBLEM-2
- 2번째 pjt를 참고해서 그래프 그리기 성공.
- x축에 상당히 많은 date 데이터가 있어서 그 부분을 관리하는게 쉽지 않았다. 아래 코드의 `MonthLocator(interval=3)` 부분이 핵심!
```py
    ax = plt.gca()
    ax.xaxis.set_major_locator(dt.MonthLocator(interval=3))
```
- 추가적인 이슈 발생과 해결과정
  - 집에서 problem3을 해결하기 위해 프로젝트를 받아온 후 작업하려고 했지만 `makemigrations` 명령어가 아래 에러메세지와 함께 정상작동하지 않는 이슈 발생
  ```
  django.db.utils.OperationalError:no such table: weathers_weather
  ```
  - migration이 안되고 서버도 열리지 않아서 데이터베이스 문제인 것으로 판단하고 db를 전부 갈아엎고 다시 migrate를 시도해도 정상동작하지 않았음.
  - 강사님께 여쭤본 결과 `import` 관련 이슈였음을 확인함.
  - 기존에는 아래의 코드를 `views.py` 함수의 전역에 두고 사용했음. 이유는 자주 재사용 될 것 같아서 쓰기 편하려고.. 근데 이렇게 전역에 db를 건드리는 코드를 작성하면 django가 새로운 환경에서 동작하기 전 모든 코드가 정상동작하는지 확인하는 과정에서 오류가 발생하게 된다.
  - 단순히 말해서 장고가 프로젝트 동작 전 views.py를 실행해보는데 새로운 환경에서는 db가 migrate 되기 전이니 `db가 없어!` 라고 소리지르는 것이다.
  - 그렇다면 어떻게 해결할 수 있는가? 전역에 작성한 코드를 함수로 만들어 준 후 `df`를 리턴하여 그걸 다른 함수에서 받아서 사용하도록 하면 됨.
  ```py
  csv_path = 'weathers/data/austin_weather.csv'
    df = pd.read_csv(csv_path)

    for index,row in df.iterrows():
        if Weather.objects.filter(date=row['Date']).exists(): continue
        weather = Weather(
            date = row['Date'],
            temp_high_f = row['TempHighF'],
            temp_avg_f = row['TempAvgF'],
            temp_low_f = row['TempLowF'],
            dew_point_high_f = row['DewPointHighF'] if row['DewPointHighF'] != '-' else 0,
            dew_point_avg_f = row['DewPointAvgF'] if row['DewPointAvgF'] != '-' else 0,
            dew_point_low_f = row['DewPointLowF'] if row['DewPointLowF'] != '-' else 0,
            humidity_high_percent = row['HumidityHighPercent'] if row['HumidityHighPercent'] != '-' else 0,
            humidity_avg_percent = row['HumidityAvgPercent'] if row['HumidityAvgPercent'] != '-' else 0,
            humidity_low_percent = row['HumidityLowPercent'] if row['HumidityLowPercent'] != '-' else 0,
            sea_level_p_high_inches = row['SeaLevelPressureHighInches'] if row['SeaLevelPressureHighInches'] != '-' else 0,
            sea_level_p_avg_inches = row['SeaLevelPressureAvgInches'] if row['SeaLevelPressureAvgInches'] != '-' else 0,
            sea_level_p_low_inches = row['SeaLevelPressureLowInches'] if row['SeaLevelPressureLowInches'] != '-' else 0,
            events = row['Events'],
        )
        weather.save()
  ```

### PROBLEM-3
- 2번째 pjt에서 사용했던 월별 groupby를 아무리 적용하려고 해도 실패했다..
- 완전하지 않은 csv 파일이기 때문인 것으로 추측하고 있음
- 정수형 field인데 '-'로 들어오는 데이터를 0으로 받도록 모델을 설계했는데 그게 문제인건가? 에러 메세지 중 아래의 메세지가 `monthly_data = df.groupby(df['Date'].dt.to_period('M')).mean()` 해당 코드에서 계속 발생했음.. 데이터 셋의 row 를 column을 신경쓰지 않고 계산하려고 하는 것 같은데 추후 확인이 필요함. 
```py
TypeError: Could not convert string '6743313644394143493131' to numeric
```

## 최종
- pandas 단순해 보였는데 엄청 복잡하다.. groupby 이거 더 공부해야할 듯. 찾아보니까 엄청 자주 사용하는 메서드라고 한다.