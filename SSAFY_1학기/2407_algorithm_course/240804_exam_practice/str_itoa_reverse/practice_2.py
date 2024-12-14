# 123 -> '123'
# ord() -> str에 대응되는 ASCII 정수를 리턴
# chr() -> ASCII 정수에 대응되는 str 리턴
def itoa(integer):
    '''
    1. 1의 자리 수를 차례대로 str으로 변환 후 list에 담기
    2. 해당 리스트를 뒤집어 리턴
    '''
    result_string = ''
    while integer > 9:
        digit = integer % 10
        str_digit = chr((ord('0') + digit))
        result_string += str_digit
        integer = integer // 10
        while integer > 0:
            digit = integer % 10
            str_digit = chr((ord('0') + digit))
            result_string += str_digit
            integer = integer // 10

    reversed_string = reverse_string(result_string)
    return reversed_string
def reverse_string(string):
    result_str = ''
    # for i in range(1,len(string)+1):
    #     result_str += string[-i]
    for i in range(len(string) - 1, -1, -1): # 길이-1 부터 0까지 1씩 줄어드는 i -> 8,7,6,5,4,3,2,1,0
        result_str += string[i]
    return result_str

int_input = 123456789
print(itoa(int_input))
print(type(itoa(int_input)))