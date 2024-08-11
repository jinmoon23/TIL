'''
수강생이 N명
수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램
수강생의 수를 나타내는 정수 N(2≤N≤100)과 과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분
두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.

문제접근
1. students 정수를 받아 1부터 시작하여 students까지의 연속된 정수 리스트를 생성한다.
2. 다음줄에서 주어지는 제출자의 번호를 위 리스트에서 삭제한다. -> remove나 pop을 사용하니 인덱스 에러가 자주 발생.
    -> F_list 를 생성해 포함되어 있지 않는 elem만 찾아서 담아 해결.
3. 담은 후의 리스트를 오름차순 정렬 후 리턴한다.
'''
import sys
sys.stdin = open("sample_input.txt", "r")

def find_F(students_list,submits_list):
    F_list = []
    for number in students_list:
        if number not in submits_list:
            F_list.append(number)

    for i in range(len(F_list)-1):
        if F_list[i] > F_list[i+1]:
            F_list[i],F_list[i+1] = F_list[i+1], F_list[i]
    for elem in F_list:
        print(elem,end=' ')
    return ''


T = int(input())
for test_case in range(1, T + 1):
    students, submits = map(int,input().split())
    submits_number = list(map(int,input().split()))

    students_number_list = []
    for i in range(1,students+1):
        students_number_list.append(i)

    print(f'#{test_case}',end=' ')
    print(find_F(students_number_list,submits_number))