def check_match(expression):
    stack = []  # 스택을 빈 리스트로 초기화
    # 괄호 짝을 맞추기 위한 사전
    matching_dict = {')': '(', '}': '{', ']': '['}

    for char in expression:  # 문자열의 각 문자를 순회
        if char in matching_dict.values():  # 열린 괄호를 만나면
            stack.append(char)  # 스택에 추가
        elif char in matching_dict.keys():  # 닫힌 괄호를 만나면
            # 스택이 비어있거나 짝이 맞지 않으면 괄호가 맞지 않으므로 False 반환
            if not stack or stack[-1] != matching_dict[char]:
                return False
                # 짝이 맞으므로 스택에서 가장 위의 아이템 제거
            stack.pop()

    # 스택이 비었다면 제대로 짝이 맞은 거기 떄문에 True
    if len(stack) == 0:
        return True

    return False  # 스택이 비어있지 않다면, 닫힌 괄호가 덜 나왔다는 의미이다. 그러므로 False

# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")
