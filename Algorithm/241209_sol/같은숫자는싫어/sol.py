# 1. arr을 순회
# 2. stack에 값이 없으면 append
# 3. stack에 값이 있고 stack의 마지막 값이 elem 값과 같지 않다면 append
# 4. stack 반환

def solution(arr):
    stack = []
    for elem in arr:
        if stack:
            if stack[-1] != elem:
                stack.append(elem)
            # stack[-1] == elem의 경우 아무런 동작을 하지 않고 다음 순회로 넘어감
        else:
            stack.append(elem)
    return stack