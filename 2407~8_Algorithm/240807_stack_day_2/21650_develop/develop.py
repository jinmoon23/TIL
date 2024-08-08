'''
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
순서대로 작업의 진도가 적힌 정수 배열 progresses
각 작업의 개발 속도가 적힌 정수 배열 speeds
각 배포마다 몇 개의 기능이 배포되는지를 return

배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
ex) [93, 30, 55] [1,30,5] -> [2,1]
1. 1일 후 [94,60,60] / 2일 후 [95,90,65] / 3일 후 [96,100,70] / 4일 후 [97,100,75] / 5일 후 [98,100,80] / 6일 후 [99,100,85] / 7일 후 [100,100,90] 1배포 / 8일 후 [95] / 9일 후 [100] 1배포 -> [2,1]
ex) [95, 90, 99, 99, 80, 99] [1, 1, 1, 1, 1, 1]  -> [1, 3, 2]

문제의 핵심
1. 하루 1배포
2. progresses 배열의 앞 인덱스부터 완료 되어야만 배포가능.
3. 배포 시 몇 개의 기능이 배포되는가?

접근 아이디어
1. 잔여 작업일수를 list 형태로 정리한 후 elem의 부등호 상태에 따라 따로 설정한 리스트에 저장 후 길이 리턴
2. residual_day_list[i] >= residual_day_list[i+j] 인 경우 residual_day_list[i] < residual_day_list[i+j]를 충족할 때 까지의 모든 값을 따로 설정한 2차원배열에 넣고싶다.
    ex) [10,1,1,20] 의 경우 [[10,1,1],[20]] 이런 방식으로.
3.
'''

def solution(progresses, speeds):
    answer = []
    residual_working_list = [] # 잔여 작업률 구하기
    residual_day_list = [] # 잔여 작업일수 구하기

    for progress in progresses:
        residual_working_list.append(100-progress)

    for i in range(len(residual_working_list)):
        if residual_working_list[i] % speeds[i] == 0:
            residual_day_list.append(residual_working_list[i] // speeds[i])
        else:
            residual_day_list.append((residual_working_list[i] // speeds[i])+1)
    # 여기까지 잔여 작업일수 구하는 코드

    stack =[]

    for i in range(len(residual_day_list)):
        if not stack:
            stack.append(residual_day_list[i])
        else:
            if stack[0] >= residual_day_list[i]:
                stack.append(residual_day_list[i])
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(residual_day_list[i]) # 스택 관리의 핵심
        if i == len(residual_day_list)-1: # 탐색이 마무리된 경우 처리
            if stack:
                answer.append(len(stack))

    return answer


# print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))