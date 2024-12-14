import sys
sys.stdin = open('input.txt', encoding='utf-8')

"""
문자열: ABCDABCDABC
패턴: ABCD
"""
for _ in range(10):
    tc = int(input())
    pattern = input()
    search_text = input()
    result = 0   # 패턴 일치 횟수

    # 비교할 부분을 가리키는 패턴의 인덱스
    # 비교할 부분을 가리키는 문자열의 인덱스
    pattern_idx = 0
    compare_idx = 0

    # 버블정렬처럼 찾으려고 하는 문자열의 처음부터 시작해서 문자열의 끝까지 진행
    while compare_idx < len(search_text):
        # 패턴이 다른 경우
        if search_text[compare_idx] != pattern[pattern_idx]:
            # 여태까지 비교해온 패턴만큼 뒤로가서 다시 시작
            compare_idx = compare_idx - pattern_idx + 1
            pattern_idx = 0
            continue

        # 패턴이 같은 경우에는
        # 패턴의 위치도 한 칸 앞으로
        # 현재 비교해야하는 문자도 한 칸 앞으로
        pattern_idx += 1
        compare_idx += 1

        # 모든 문자열을 비교한 경우
        if pattern_idx == len(pattern):
            result += 1  # 패턴 찾은 거 기록
            pattern_idx = 0  # 패턴은 처음 위치부터 다시 비교 시작
            compare_idx = compare_idx - pattern_idx + 1  # 패턴의 길이만큼 뒤로 간 후 한 칸 앞으로 이동해서 다시 검색 시작

    print(f"#{tc} {result}")
