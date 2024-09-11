def trip(start, dictionary, arr, visited):

    for i in range(len(dictionary[start])):     # 딕셔너리의 도착 공항 리스트 길이만큼 반복
        if visited[start][i]:   # 이미 사용한 항공편이라면(ex. "ICN" -> "ATL") continue
            continue
        # 다음으로 출발할 항공편의 도착 공항이 없다면(다음으로 갈 곳이 없다면, ex. "ICN" -> "AAA" -> "") continue
        if not dictionary[dictionary[start][i]]:
            continue
        arr.append(dictionary[start][i])    # arr(path, 경로)에 도착 공항을 추가
        visited[start][i] = 1   # 항공편을 사용했다고 표기(ex. visited = {"ICN" : [1, 0], ...})
        trip(dictionary[start][i], dictionary, arr, visited)    # 그 다음 항공편에 대하여 재귀

    return arr  # arr(path) return


def solution(tickets):
    airport_dict = {}   # 출발 공항과 도착 공항을 기록한 딕셔너리
    visited = {}    # 도착 공항의 방문 표시를 위한 딕셔너리

    for ticket in tickets:  # 항공편을 반복하고
        for airport in ticket:  # 항공편의 공항을 반복하며
            if airport not in airport_dict:  # 딕셔너리에 공항명이 없다면
                airport_dict.setdefault(airport, [])    # 공항명을 key로 하고 빈 리스트를 value로 하여 추가
                visited.setdefault(airport, [])     # visited도 공항명을 key로 하고 빈 리스트를 value로 하여 추가

    for ticket in tickets:
        airport_dict[ticket[0]].append(ticket[1])   # 출발 공항을 key로 할 때 도착 공항을 value에 추가
        visited[ticket[0]].append(0)    # visited도 출발 공항을 key로 할 때 value에 도착 공항의 수 만큼 0 추가

    # airport_dict = {'SFO': ['ATL'], 'ATL': ['ICN', 'SFO'], 'ICN': ['ATL', 'SFO']}
    # visited = {'SFO': [0], 'ATL': [0, 0], 'ICN': [0, 0]}

    for keys in airport_dict.keys():
        airport_dict[keys].sort()   # 도착 공항을 알파벳 순으로 정렬

    # print(visited)
    # print(airport_dict)

    path = ["ICN"]  # 시작 공항을 기록, 항상 인천 공항에서 출발하므로 "ICN" 저장
    answer = trip("ICN", airport_dict, path, visited)   # 출발 공항과 공항 딕셔너리, 경로, visited를 매개변수로 DFS

    for keys in airport_dict.keys():
        for i in range(len(airport_dict[keys])):
            if not visited[keys][i]:    # 사용하지 않은 항공편이 있다면
                answer.append(airport_dict[keys][i])    # 마지막으로 경로에 추가
    return answer