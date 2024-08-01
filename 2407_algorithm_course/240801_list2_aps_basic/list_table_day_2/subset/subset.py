arr = [1,2,3]
n = len(arr)
subset_cnt = 2**n

subsets = [] # 부분집합이 모이는 리스트
for i in range(subset_cnt): # 0~7까지 순회
    subset = [] # 부분집합 임시 저장소
    for j in range(n):
        if i & (1 << j): # i = 0인 경우 if문을 통과할 수 없어서 subsets.append(subset) 로 이동 후 공집합이 저장됨
            subset.append(arr[j])
    subsets.append(subset)

print(subsets)