data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * (max(data)+1) # 0~4 까지의 정수
print(counts)
result = [0] * len(data)

for elem in data:
    counts[elem] += 1 # 1단계, data의 원소 i를 가져와서 counts[i]에 개수 기록
print('1단계', counts) #[1,3,1,1,2]

# for i in range(len(data)): # 해당 코드와 위 코드는 동일한 메커니즘을 가짐
#     counts[data[i]] += 1

for i in range(1, max(data)+1):
    counts[i] = counts[i]+counts[i-1] # 2단계, 누적 개수
print('2단계', counts)

for i in range(len(data)-1, -1, -1):
    counts[data[i]] -= 1 # 누적 개수 1개 감소
    result[counts[data[i]]] = data[i]

print('최종', *result) # 0 1 1 1 2 3 4 4