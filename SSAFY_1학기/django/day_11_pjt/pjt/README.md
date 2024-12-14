# 05-pjt

해결한 과제
1. keyword.html
2. keyword/pk.html
3. keyword/crawling.html
4. keyword/crawling_histogram.html

어려웠던 점
1. crawling 진행 시 저장하려는 정보가 이미 테이블에 존재할 경우에 대한 분기처리가 어려웠다. 결국 해결하지 못함..
- 이 부분 추가적으로 작업해 완성하였음!
```py
# 기존의 코드
trend, created_trend = Trend.objects.get_or_create(name=name,result=result,search_period=search_period)
# 변경된 후의 코드
trend, created_trend = Trend.objects.get_or_create(name=name, defaults={
    'result': result, 'search_period': search_period
    })

# get_or_create 메서드의 defaults 인자의 역할을 확실히 파악할 수 있었다.
# 오직 name만을 고려 요인으로 두고 나머지는 중복검사를 실시하지 않는것!
# 이 코드 변화로 인해 분기처리를 정상적으로 진행할 수 있다.
```
2. crawling 완료 후 원하는 정수값(총 검색횟수)으로 변환하는 과정이 힘들었다. 이건 성공!
3. 키워드 저장하는 부분에서 동일한 키워드 네임으로 저장되는 상황이 발생했음. 그런데 `forms.py`를 활용해 `ModelForm` 형태로 유저 입력값을 처리하기 때문에 어떻게 그 키워드 네임에 접근해야할지 난감했다.
   - 이는 form의 유효성검사와 cleaned_data 및 get()을 활용해 해결했다.
```py
form = KeywordForm(request.POST)
    if form.is_valid():
        # 유효성 검사를 완료한 경우에만 cleaned_data로 접근이 가능하고 이후 get() 메서드로 form 내부의 속성인 키값인 name에 접근할 수 있었다.
        name = form.cleaned_data.get('name')
        # 여기서 get이 아닌 filter를 사용하는 이유는 해당하는 name 필드가 애초에 존재하지 않았던 경우에도 에러가 발생하지 않도록 하기 위함이다. 
        if not Keyword.objects.filter(name=name).exists():
            form.save()
            return redirect('trends:keyword')
        else:
            form.add_error('name','이미 존재하는 키워드입니다.')
```

느낀점
1. crawling의 핵심적인 데이터 받아오기를 성공해서 뿌듯했지만 만족스럽게 분기처리를 하지 못한것이 아쉽다. 디테일한 부분을 더 공부하도록 해야겠다 ^_^
2. 확실히 시각화 부분(matplotlib)은 반복되는 파트가 많다. 익숙해지는것도 물론 중요하겠지만 영리하게 찾아보고 적용할 수 있어야겠다.