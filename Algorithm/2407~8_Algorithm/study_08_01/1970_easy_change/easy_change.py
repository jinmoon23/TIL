import sys
sys.stdin = open("input.txt", "r")

def min_change(change):

    change_dict = {
        50000:0,
        10000:0,
        5000:0,
        1000:0,
        500:0,
        100:0,
        50:0,
        10:0
    }

    for key in change_dict.keys():
        change_dict[key] = change // key
        change = change % key

    result_list = []

    for value in change_dict.values():
        result_list.append(value)

    result = list(map(str,result_list))
    return ' '.join(result)

T = int(input())
for test_case in range(1, T + 1):
    change = int(input())
    print(f'#{test_case}')
    print(min_change(change))


'''
가현님 코드리뷰
- mon,inp 변수명이 직관적이지 못합니다! 조금 더 직관적인 변수명을 작성하시면 좋을 것 같습니다.
- mon은 안써도 될 것 같습니다?!
- gpt의 도움을 아이디어적으로 받은건지 아이디어는 제시하고 그에 따른 코드를 받은 건지 궁금합니다. 아이디어는 접근이 참 좋아보여요.
- -로 접근한 것도 좋지만 % 연산자로 나머지 접근도 추천드립니다. 
'''