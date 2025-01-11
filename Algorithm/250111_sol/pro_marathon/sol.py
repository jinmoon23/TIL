'''
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
동명이인이 있을 수 있다.

1. p 리스트의 요소 1개에 대해 c 리스트의 값 전부를 순회
2. 동일한 요소 발견 시 해당 값 제거 및 순회 종료
3. p 리스트의 길이가 1이 될 때까지 해당 순회 후 값 반환
'''

def solution(participant, completion):
    for p in participant:
        if p not in completion:
            return p
        elif p in completion and participant.count(p) > completion.count(p):
            return p




print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))




