def f(i,N): # i: 현재 인덱스 / N: 크기
    if i == N:
        return
    else:
        print(arr[i])
        f(i+1,N)

arr = [1,2,3]
f(0,3)