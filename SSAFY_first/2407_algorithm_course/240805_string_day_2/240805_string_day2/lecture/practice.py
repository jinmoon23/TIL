'''
1. 패턴매칭
    - 고지식한 패턴 검색(brute force)
    - 카프-라빈
    - KMP
    - 보이어-무어
2.
'''
# 고지식한 패턴 검색
t = 'TTTTTABC'
p = 'TTA'
N = len(t)
M = len(p)
count = 0
for i in range(N-M+1): # 비교 시작 위치, i = 0,1,2,3,4
    for j in range(M):
        if t[i+j] != p[j]:
            break  # for j, 다음 글자부터 비교 시작
    else: # for j가 중단없이 반복되면
        count += 1
print(count)

