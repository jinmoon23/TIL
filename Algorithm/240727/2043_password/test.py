num1, num2 = map(int,input().split())

def find_password(num1,num2):
    result_count = 0
    # 입력과 동시에 1번의 확인
    if num2 == num1:
        result_count = 1
        return result_count
    else: 
        result_count = 1 # 확인 결과 같지 않으면 카운트 + 1
    # 비밀번호를 찾을 때 까지 카운트 지속
    while num2 != num1:
        result_count += 1
        num2 += 1
    return result_count

print(find_password(num1,num2))