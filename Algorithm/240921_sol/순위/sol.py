'''
1번부터 n번까지 번호를 받았습니다.
하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
정확하게 순위를 매길 수 있는 선수의 수를 return
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
'''
def solution(n, results):
    paths = [[] for _ in range(n+1)]
    for w,l in results:
        paths[w].append(l)
    print(paths)
    answer = 0
    return answer