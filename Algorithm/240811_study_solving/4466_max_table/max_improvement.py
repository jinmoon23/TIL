'''
N개의 과목에 대한 시험을 쳤다. 각 과목의 점수는 정수이고 만점은 100점이다.
성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다.
당신은 기왕이면 성적표에 나타나는 총점이 가장 크도록 성적표를 만들고 싶다.
최대로 만들 수 있는 총점은 몇점인지 구하여라.

문제접근
1.N개 중 K개의 원소를 가지는 부분집합을 구하고
2. 그 부분집합의 합 중 가장 큰 값을 리턴한다.

문제발생
- 제한시간초과가 발생함 -> 추측: 모든 부분집합을 만드는 과정에서 많은 시간이 소요되는 듯.
- 해결방법은 무엇일까? 그냥 잘못된 접근인걸까?

개선된 접근법
입력으로 받은 point_arr를 내림차순으로 정렬 후 0번 인덱스부터 choice+1까지의 값을 더해 리턴한다.
'''
import sys
sys.stdin = open("sample_input.txt", "r")

def find_max_sum(arr):
    for i in range(point_number-1,0,-1): # point_number가 3인 경우 2번만 버블소팅 진행해도 됨. 2와 1이 i에 들어감
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j] # 버블소팅 내림차순 정렬

    return sum(arr[:choice]) # 슬라이싱을 활용한 리턴

T = int(input())
for test_case in range(1, T + 1):
    point_number,choice = map(int,input().split())
    point_arr = list(map(int, input().split()))
    print(f'#{test_case} {find_max_sum(point_arr)}')
