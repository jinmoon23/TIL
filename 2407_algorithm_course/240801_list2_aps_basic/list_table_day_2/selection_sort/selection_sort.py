# selection sort
# 가장 작은 값의 인덱스를 기본값(0)으로 설정한 후
# 배열을 순회하며 더 작은 값을 찾으면 그 값의 인덱스를 min_index 변수에 재할당한다.
# 그 후 최소값의 자리를 변경하여 sorting을 계속함.
# 예를들어 [3,7,5,2,4]의 경우 3(arr[min_index])과 7,5,2,4를 순차적으로 순회하며 2를 만나게 되어 if 이하의 코드가 실행되면
# min_index가 0에서 2의 인덱스인 3으로 변경된다.
# 그리고 arr[i],arr[min_index] = arr[min_index], arr[i] 코드를 통해 3을 2로, 2를 3으로 변경하게된다.

def selection_sort(arr,N): # arr: 정렬대상 , N: 리스트 길이
    # 주어진 구간에 대해 기준위치 i를 정하고
    for i in range(N-1):
        min_index = i # 최솟값 위치를 기준위치로 가정
        for j in range(i+1,N): # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i] # i임에 주의
    return arr

a = [3,7,5,2,4]
print(selection_sort(a,len(a)))
