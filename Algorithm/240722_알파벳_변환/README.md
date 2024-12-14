# 알파벳 변환

## 문제분석
1. 알파벳 문자열 A와 정수형 1을 대응하자
2. 그리고 if문으로 정리하자.
3. 정말 긴 시간이 걸렸다..

## 풀이
1. 직접 만든 alpa_list와 입력값 t(list)를 순회
2. A(alpa_list)와 A(t)가 같으면 alpa_list에서 A를 찾은 후 그 index+1을 리턴받아 임의로 만든 result_list에 할당

1번째 반복
A vs B / A vs C / A vs F -> 맞는것이 없으니 다음 반복으로 넘어감
2번째 반복
B vs B -> True -> alpa_list의 B값을 찾아 인덱스를 구하고 그 값에 +1한 값을 result_list에 할당함. index+1은 index니까!

아래는 고민의 흔적
```py
t = [B,C,F] # [A,B,C...] 
alpa_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# def check(t):
#     result_list = []
#     for char in alpa_list:
#         if char == 'A':
#             result_dict[char] = num_list[num_list.index(1)]
#         elif char == 'B':
#             result_dict[char] = num_list[num_list.index(2)]
#         elif char == 'C':
#             result_dict[char] = num_list[num_list.index(3)]
#     for char in t:
#         if char == 'A':
#             result_list.append(result_dict[char])
#         elif char == 'B':
#             result_list.append(result_dict[char])

#     return result_list

def check(t):
    result_list = []
    # for char in alpa_list:
    #     if char == 'A':
    #         result_dict[char] = num_list[num_list.index(1)]
    #     elif char == 'B':
    #         result_dict[char] = num_list[num_list.index(2)]
    #     elif char == 'C':
    #         result_dict[char] = num_list[num_list.index(3)]
    # for char in t:
    #     if char == 'A':
    #         result_list.append(result_dict[char])
    #     elif char == 'B':
    #         result_list.append(result_dict[char])
    
    for char in alpa_list:
        for i in t:
            if char == i:
                result_list.append(alpa_list.index(i)+1)


    return result_list




print(check(t))
```

## 생각할 점
```py
for i in t:
    for char in alpa_list:
# 아래는 fail 위는 pass 차이는 무엇?
for char in alpa_list:
        for i in t:








# 추측컨데 내가 입력한 값을 비교를 위해 설정한 값들 전체와 비교하지 않았기 때문이 아닐까 싶다. 그런데 vscode 내에서 출력값은 동일함. swea에서만 출력값이 달라진다. 이 부분은 왜 그런걸까? 
```