# 이 문제 왜이래? 우선순위라고 해놓고 숫자가 클 수록 우선순위가 높다고 함,, 거꾸로 여야지
# 1. priorities 배열을 순회
# 2. elem 보다 큰 숫자가 priorities 배열에 있으면 leftpop & append(leftpop)

def solution(priorities, location):
    # 이런 방식으로 새로운 배열을 만들 수 있군,,
    # 미리 대기큐의 인덱스를 받는다.
    priorities1 = [[i,x] for i,x in enumerate(priorities)]
    result = []
    while priorities1:
        i,x = priorities1.pop(0)
        # y는 비교할 대상
        for j,y in priorities1:
            # x는 기존의 pop 한 대상
            # 우선순위가 빠른 프로세스가 있으므로 다시 대기큐에 넣는다.
            if y > x:
                priorities1.append([i,x])
                break
        # pop한 프로세스 보다 더 우선순위가 빠른 프로세스가 없으므로 최종 result 배열에 넣는다.
        else:
            result.append([i,x])
    for i,arr in enumerate(result):
        # 미리 인식해 두었던 index와 찾고자 하는 index(location)이 같을 경우 result 배열의 index에 +1 하여 리턴.
        if arr[0] == location:
            return i+1

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
print(solution([1,2,3,4,5],3))
