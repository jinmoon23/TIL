def solution(participant, completion):
    # 해당 함수가 시작되고 종료되기 까지 한 번 정의된 hash 값은 변하지 않는다.
    # 따라서 hash_sum 변수에 hash 값을 일정하게 더하거나 빼서 마지막에 해당 hash_sum 값을 key로 name_dict 딕셔너리의 값을 찾을 수 있다.
    hash_sum = 0
    name_dict = {}

    for name in participant:
        hash_sum += hash(name)
        name_dict[hash(name)] = name
    for name in completion:
        # 마지막에 남겨질 hash_sum을 도출하기 위해 위에서 더했다면 빼고 뺐다면 더한다.
        hash_sum -= hash(name)
    return name_dict[hash_sum]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))