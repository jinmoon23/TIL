'''
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.
번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

문제접근
1. 입력받은 문자열을 앞에서부터 순회하며 동일한 문자가 2회 반복될 경우 그 둘을 소거
2. 1의 문자열을 다시 앞에서부터 순회하며 반복
3. 모든 문자열을 순회해도 반복되는 문자가 발견되지 않는 경우 해당 문자열을 리턴
'''

import sys
sys.stdin = open("input-6.txt", "r")

def pwd_generator(N,pwd_can):
    for index,can in enumerate(pwd_can): # enumerate를 사용해 인덱스에 상응하는 값 모두를 활용
        for i in range(N): # 하나의 값에 대해 그 다음 값과 비교하기 위해 2중 for문 사용
            if i <= index: continue # 지나온 값들을 비교할 필요 없으니 elary return 처리
            if can == pwd_can[i]:
                pwd_can.pop(index)
                pwd_can.pop(index)
                N -= 2 # 인덱스에러를 방지하고 재귀호출 시 N을 수정된 상태로 사용하기 위함
                break
            else:
                break # 연속된 한 쌍의 값이 서로 다르다면 굳이 추가적인 확인의 과정이 필요하지 않기 때문에 break
                      # 쉽게말해 [1,3,5,4,4]가 있는 경우 1,3을 확인 3,5를 확인, 5,4를 확인, 4,4를 확인하기 위함
    else: # 가장 위의 for문이 종료된 후 남아있는 쌍값을 소거하기 위해 for - else 사용
        for i in range(N-1):
            if pwd_can[i] != pwd_can[i+1]: continue # 연속된 값들을 확인함.
            else: # 만약 같은값이 한쌍이라도 있다면 아직 비밀번호 생성이 완료되지 않은 것.
                return pwd_generator(N, pwd_can) # 비밀번호가 생성될 때까지 재귀호출
        else: # for문이 모두 종료된 경우에도 재귀호출이 되지 않았다는 것은 의도한대로 비밀번호가 생성되었다는 것이므로 return하고 함수 종료.
            return ''.join(pwd_can)

T = 10
for test_case in range(1, T + 1):
    N,string = input().split() # 비밀번호 후보의 길이(str) / 비밀번호 후보(str)
    pwd_can = [] # 입력으로 받은 문자열 덩어리를 가공하기 편하게 리스트로 변환. (pop과 enumerate를 사용하기 위함)
    for char in string:
        pwd_can.append(char)
    print(f'#{test_case} {pwd_generator(int(N),pwd_can)}')
