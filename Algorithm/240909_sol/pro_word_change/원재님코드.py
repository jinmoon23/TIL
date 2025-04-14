"""
begin = "hot"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin에서 target을 만드는 데 한 번에 한 알파벳만 바꿀 수 있습니다.
저는 문제를 보고, 단어들을 비교하며 한 글자 씩 달라지는 경우 끼리 연결하여 그래프를 만들었습니다.
그렇게 그래프를 만들어 BFS를 통해 begin에서 target까지 최단 거리를 구해야겠다고 접근했습니다.
"""

from collections import deque


def solution(begin, target, words):
    answer = 0  # begin에서 target까지의 최단 거리
    word_dict = {}  # 인접 리스트를 표현할 딕셔너리
    words.append(begin)  # 한 알파벳만 차이나는 경우를 구하기 위해 words에 begin을 포함시킨다.
    N = len(words)

    visited = set()  # 이미 방문한 곳을 제외하기 위한 visited set
    dist = {}   # 거리를 기록하기 위한 딕셔너리

    def word_change(start):
        visited.add(start)  # 시작점(begin) 방문 표시
        dist[start] = 0  # 시작점은 거리가 0
        queue = deque()
        queue.append(start)

        while queue:
            next_word = queue.popleft()
            for word in word_dict[next_word]:   # 단어에서 다음 단계로 갈 수 있는 단어들을 반복하며
                if word in visited: continue    # 방문한 적 있는 단어라면 continue
                visited.add(word)   # 아니라면 visited에 추가
                queue.append(word)
                dist[word] = dist[next_word] + 1    # 전에 바뀐 단어까지 걸린 단계 수 + 1

    # 단어의 인접 리스트를 만들기 위한 코드
    for word in words:
        word_dict[word] = []    # 단어를 key로 하고 value에 빈 리스트 생성
        dist[word] = 0  # 단어를 key로 하고 value에 0을 생성
        for comp in words:  # 단어와 words의 다른 단어들과 비교하여
            if word == comp: continue   # 같으면 continue
            cnt = 0  # 차이나는 알파벳 개수
            for i in range(len(begin)):  # 단어 길이만큼 반복하며
                if word[i] != comp[i]:  # 두 단어를 비교하여 알파벳이 차이나면
                    cnt += 1    # cnt + 1
                if cnt > 1: continue    # cnt가 1을 넘어가면 continue
            else:
                if cnt == 1:    # 최종적으로 차이나는 알파벳 개수가 1개이면
                    word_dict[word].append(comp)    # 단어를 key로 하는 리스트에 추가
    # 위 코드의 결과
    # word_dict = {'hot': ['dot', 'lot', 'hit'], 'dot': ['hot', 'dog', 'lot'],
    #              'dog': ['dot', 'log', 'cog'], 'lot': ['hot', 'dot', 'log'],
    #              'log': ['dog', 'lot', 'cog'], 'cog': ['dog', 'log'],
    #              'hit': ['hot']}
    # dist = {'hot': 0, 'dot': 0, 'dog': 0, 'lot': 0, 'log': 0, 'cog': 0, 'hit': 0}
    print(word_dict)
    print(dist)
    word_change(begin)  # BFS
    if target not in words:  # words에 target이 없다면
        answer = 0
    else:   # 있다면
        answer = dist[target]   # target까지 걸린 거리를 출력

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))