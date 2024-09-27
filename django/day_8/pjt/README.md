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

### PROBLEM-3
- 2번째 pjt에서 사용했던 월별 groupby를 아무리 적용하려고 해도 실패했다..
- 완전하지 않은 csv 파일이기 때문인 것으로 추측하고 있음
- 정수형 field인데 '-'로 들어오는 데이터를 0으로 받도록 모델을 설계했는데 그게 문제인건가? 에러 메세지 중 아래의 메세지가 `monthly_data = df.groupby(df['Date'].dt.to_period('M')).mean()` 해당 코드에서 계속 발생했음.. 데이터 셋의 row 를 column을 신경쓰지 않고 계산하려고 하는 것 같은데 추후 확인이 필요함. 
```py
TypeError: Could not convert string '6743313644394143493131' to numeric
```

## 최종
- pandas 단순해 보였는데 엄청 복잡하다.. groupby 이거 더 공부해야할 듯. 찾아보니까 엄청 자주 사용하는 메서드라고 한다.