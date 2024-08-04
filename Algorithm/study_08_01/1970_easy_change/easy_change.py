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