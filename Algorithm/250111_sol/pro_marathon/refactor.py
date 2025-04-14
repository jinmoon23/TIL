from collections import Counter

def solution(participant, completion):
    # Counter 객체를 사용하여 각 이름의 등장 횟수를 계산
    # participant 리스트를 순회하면서 요소를 key로 리스트 내 요소의 등장 횟수를 value로 가지는 딕셔너리 클래스
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    # 두 Counter 객체의 차이를 계산
    # 딕셔너리 간 더히기 빼기 연산은 불가능하지만 Counter는 딕셔너리의 하위 클래스로서 해당 연산이 가능하다.
    # 추가적으로 Counter 클래스는 더하기 빼기와 합집합 교집합 연산이 가능하다.
    diff = participant_count - completion_count
    # 차이가 나는 이름(완주하지 못한 선수)을 반환
    return list(diff.keys())[0]

# print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))