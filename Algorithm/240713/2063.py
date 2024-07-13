N = int(input())

    # N 개의 점수를 입력받습니다.
numbers = list(map(int, input().split()))

    # 점수를 정렬합니다.
sorted_numbers = sorted(numbers)

    # 중간값의 인덱스를 계산합니다.
middle_index = N // 2

    # 중간값을 출력합니다.
print(sorted_numbers[middle_index])


# 하.. 문제에 대한 해답은 일찍이 찾았는데 어떻게 제출해야 하는지 이해가 잘 안가서 엄청 고생했다..ㅠ
# 단순하게 생각하는게 답이었다. 