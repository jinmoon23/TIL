import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())   # 노선 수

for case in range(1, T+1):
    K, N, M = map(int,input().split())  # K : 한 번 충전시 갈 수 있는 최대 거리/ N : N개의 정류장 / M : 충전기 설치 대수
    elec_notion = list(map(int,input().split()))  # 충전기 설치된 정류장 배열

    notion = [0]+elec_notion+[N]  # 정류장 출발 시작 0에서부터 정류장 끝까지 탐색
    start = 0
    res = 0

    for i in range(1,M+2): # M 정류소 보다 시작과 끝 정류장 추가한만큼의 범위 설정
        if notion[i] - notion[i-1] > K:   # K만큼 이동 못하면 종료 조건 설정  K = 3 인데 [0, 10, 12] 이면 3만큼 이동 불가
            res = 0
            break
        if notion[i] - start > K:  # K만큼 커지면 그 전 충전기 설치된 곳에서 충전해야함
            start = notion[i-1]  # start값 그 전 인덱스로 다시 재할당 -> 그 전 인덱스 값은 그 전 충전소를 의미함.
            res += 1  # 충전 횟수 count
    print(f'#{case} {res}')