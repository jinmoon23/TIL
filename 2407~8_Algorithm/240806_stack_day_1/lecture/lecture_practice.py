'''
Stack
1. 스택이 공백인지 아닌지 확인하는 연산 isEmpty
2. 스택의 탑에 있는 원소를 반환하는 연산 peek
'''

# stack = []
# stack.append(1) # push(1)
# stack.append(2) # push(2)
# stack.append(3) # push(3)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

'''
스택의 응용
1. Function Call
    - 함수 호출과 복귀에 따른 실행 순서를 관리
    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 스택의 구조를 활용
'''
def f2(c,d):
    return c-d

def f1(a,b):
    c = a+b
    d = 10
    return f2(c,d)

a = 10
b = 20

print(f1(a,b))