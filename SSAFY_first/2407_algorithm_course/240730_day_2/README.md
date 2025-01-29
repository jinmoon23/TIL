# Argorithm Day 2

## 카운팅 정렬
1. counts, result 배열을 준비
2. 정렬 대상 리스트의 가장 작은값과 가장 큰값을 식별
3. (1단계) counts 배열에 정렬 대상 리스트의 원소들의 식별횟수를 저장
   1. 정렬 대상 리스트가`[0,4,1,3,1,2,4,1]`인 경우 counts는`[1,3,1,1,2]`로 저장됨
```py
data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * (max(data)+1) # 0~4 까지의 정수
result = [0] * len(data)
for elem in data:
    counts[elem] += 1 # 1단계, data의 원소 i를 가져와서 counts[i]에 개수 기록
print(counts) #[1,3,1,1,2]

for i in range(1, max(data)+1):
    counts[i] = counts[i]+counts[i-1] # 2단계, 누적 개수

for i in range(len(data)-1, -1, -1):
    counts[data[i]] -= 1 # 누적 개수 1개 감소
    result[counts[data[i]]] = data[i]

print(*result) # 0 1 1 1 2 3 4 4
```
