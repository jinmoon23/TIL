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
'''
import sys
sys.stdin = open("sample_input.txt", "r")
def find_max_subset_sum(subsets_number):
    subsets = []
    for i in range(subsets_number):
        subset = []
        for j in range(point_number):
            if i & (1 << j):
                subset.append(point_arr[j]) # 핵심 아이디어. 점수리스트의 인덱스와 대응되는 값을 subsets 배열의 값으로 만든다.
        if len(subset) == choice:
            subsets.append(subset)

    subset_sum = []
    for i in range(len(subsets)):
        subset_sum.append(sum(subsets[i]))

    max_value = subset_sum[0]
    for i in range(len(subset_sum)):
        if max_value < subset_sum[i]:
            max_value = subset_sum[i]

    return max_value

T = int(input())
for test_case in range(1, T + 1):
    point_number,choice = map(int,input().split())
    point_arr = list(map(int, input().split()))
    subsets_number = 2 ** len(point_arr)
    print(f'#{test_case} {find_max_subset_sum(subsets_number)}')
