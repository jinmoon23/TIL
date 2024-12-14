import sys
sys.stdin = open('5176_re_input.txt')

def make_tree(node):
    global l_n
    if node > SALT_NUM:
        return
    make_tree(node*2)
    l_n += 1
    tree[node] = node_val[l_n]
    make_tree(node*2+1)

T = int(input())
for tc in range(1,T+1):
    hex_str = input()
    SALT_NUM = 8
    tree = [0] * (SALT_NUM+1)
    N = int(hex_str[0])
    num_lst = [] # 10진수로 변환된 값을 담을 리스트
    for i in range(1,len(hex_str),2):
        num_lst.append(int(hex_str[i:i+2],16))
    # print(num_lst) # [10, 20, 30, 40, 50, 60, 70, 80]

    salt = []
    for i in range(1,SALT_NUM+1):
        salt.append(N*i)
    for i in range(len(num_lst)):
        num_lst[i] = num_lst[i] - salt[i]
    # print(num_lst) # [1, 2, 3, 4, 5, 6, 7, 8]

    l_n = 0
    node_val = [0]
    for num in num_lst:
        node_val.append(num % 10)
    # print(node_val) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    make_tree(1)
    mapped_tree = map(str,tree[1:])
    res = ''.join(mapped_tree)
    print(f'#{tc} {res}')



