
def check_bracket_with_stack(string_list):
    bracket_dict = {'(':')','[':']','{':'}'}
    stack = []
    for string in string_list:
        for char in string:
            if char in bracket_dict.keys(): # 얻어가야할 코드. 이런 접근방식은 처음임
                stack.append(char)
            elif char in bracket_dict.values(): # 얻어가야할 코드. 이런 접근방식은 처음임
                # 닫힌 괄호를 발견하게 되면 열린 괄호가 있는지 확인한다.
                # 만약 열린 괄호를 발견하지 못하면 early return 해도 됨!
                if not stack: # 닫힌 괄호가 식별되었는데 스택이 비어있다면 괄호수가 맞지 않으니 early return.
                    return '괄호가 매칭되지 않습니다. stack underflow error'
                if char == bracket_dict[stack[-1]]: # 괄호의 짝이 맞는지 확인.
                    stack.pop()
                else: # 괄호의 짝이 맞지 않으면 매칭오류로 early return.
                    return '괄호가 매칭되지 않습니다. stack underflow error'
    if len(stack) == 0:
        return '모든 괄호가 매칭됩니다.'

    return '괄호가 매칭되지 않습니다. stack underflow error'

examples = ["(a(b))", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    print(check_bracket_with_stack(ex))