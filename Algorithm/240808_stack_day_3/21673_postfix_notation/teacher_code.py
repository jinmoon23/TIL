"""
1. 피연산자가 자오는 경우 결과에 추가
2. 여는 괄호가 나오면 스택에 추가
3. 닫힌 괄호가 나올 경우, 열린 괄호를 만날 때까지 연산자를 꺼내서 결과에 추가
4. 연산자가 나오는 경우, 스택 가장 위에 연산자가 현재 비교하려는 연산자보다 우선순위가 높거나 같다면 스택에서 제거 후 결과에 추가
   우선순위가 낮은 연산자를 만날 때까지 4번 과정 반복 후, 현재 비교하려는 연산자를 스택에 추가
5. 모든 문자에 대해서 1~4과정을 진행한 후에 스택에 남아있는 모든 연산자를 후위표기식에 추가
"""


# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    for ch in expression:
        if ch.isnumeric():  # 숫자인 경우(피연산자인 경우)에는 그냥 후위 표기식에 추가
            postfix.append(ch)
        elif ch == '(':  # 여는 괄호인 경우, 스택에 추가
            stack.append(ch)
        elif ch == ')':  # 닫는 괄호인 경우
            top_token = stack.pop()  # 스택에서 연산자를 꺼냄,
            # 꺼낸 토큰이 바로 여는 괄호면 꺼내고 끝
            while top_token != '(':  # 여는 괄호를 만날 때까지 아래를 반복
                postfix.append(top_token)  # 후위 표기식에 추가
                top_token = stack.pop()
        else:
            # 연산자인 경우
            # - 스택에 들어 있는 연산자가 지금 검사하는 연산자보다 우선순위가 더 높은 경우, 높은 친구들을 모두 거내서 후위 표기식에 추가하고, 검사하는 연산자를 스택에 추가
            # - 숫자가 높다는 건 우선순위가 높다는 것
            # - 우선순위가 같을 경우에도 스택에서 빼는 이유는 계산할 때 왼->오 로 순서대로 진행하기 떄문에, 같은 연산자가 나오면 먼저 나오면 연사자가 시행되어야 함
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:  # 스택에 남아 있는 모든 연산자를 후위 표기식에 추가
        postfix.append(stack.pop())

    return ' '.join(postfix)  # 리스트를 문자열로 변환하여 반환


# 예시
infix_expression = "3+(2*5)-8/4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")
