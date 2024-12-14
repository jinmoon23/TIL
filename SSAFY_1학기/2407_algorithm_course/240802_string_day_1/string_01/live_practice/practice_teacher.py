# ord와 chr 사용해서 구현해보기
# 입력받은 123을 '123'으로 변환하기

# ord -> 문자열의 ASCII 값(정수형)을 반환
# chr -> ASCII 값(정수형)에 대응되는 문자열을 반환
# '0'은 ASCII 값(정수형)이 48임 '3'은 48+3 = 51임. 이걸 활용해서 해결하자. char(51) == '3'
# print(type(ord('3'))) # 정수형
# print(type(chr(51))) # 문자열

# 123 -> '123'
# #1. 123을 10으로 나눈 나머지를 문자열로 변환.
# #2. 123을 10으로 나눈 몫을 10으로 나눈 나머지를 문자열로 변환
# #3. 123을 10으로 나눈 몫을 10으로 나눈 몫을 10으로 나눈 나머지를 문자열로 변환
#
# print(type(chr(ord('0')+3))) # 문자열

def itoa(integer):
    result_list = []

    while integer > 9:
        a = chr(ord('0')+integer % 10)
        result_list.append(a)
        integer = integer // 10

    """
    while integer > 0:
        a = chr(ord('0')+integer % 10)
        result_list.append(a)
        integer = integer // 10
        
    아래 9이하일때를 날리고, 위에서 while문안에 integer > 0 으로 해도 똑같이 돌아갈 것 같네요 
    """
    if integer <= 9:
        a = chr(ord('0') + integer % 10)
        result_list.append(a)

    result = ''.join(result_list)
    result_reversed = reverse_for_string(result)
    print(type(result_reversed))

    return result_reversed

# ex, '321'
def reverse_for_string(str):
    reversed_str_list = []

    for i in range(1, len(str)+1):
        reversed_str_list.append(str[-i])

    """
    위에 방법도 좋고, 아래도 동일한 코드로 될 것 같습니다. ( 작성하신 방법도 훌륭하십니다 ~ ) 
    for i in range(len(str) - 1, -1, -1):
        reversed_str_list.append(str[i])
        
    추가로 이 함수에서 파라미터 변수명으로 str 을 쓰셨는데,
    str은 파이썬에서 형변환 내장함수와 이름이 똑같은 예약어이기 때문에, 다른 변수명을 사용하는 게 더 좋아보입니다.
    (https://docs.python.org/ko/3/library/stdtypes.html)
    """

    # join 사용 굿
    reversed_str = ''.join(reversed_str_list)
    return reversed_str

i = int(input())
print(itoa(i))
