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

    for i in range(1,len(str)+1):
        reversed_str_list.append(str[-i])

    reversed_str = ''.join(reversed_str_list)
    return reversed_str

i = int(input())
print(itoa(i))
