'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

T=int(input()) # 테스트케이스 개수

for i in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_elem = arr[0]
    min_elem = arr[0]

    for elem in arr:
        if max_elem < elem:
            max_elem = elem
        elif min_elem > elem:
            min_elem = elem

    result = max_elem - min_elem
    print(f'#{i} {result}')




