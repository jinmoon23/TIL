from functools import cmp_to_key

def compare(a,b):
  order1 = a + b
  order2 = b + a
  # 610 > 106 -> 6이 먼저와야 함 -> 내림차순
  if order1 > order2:
    return -1
  elif order1 < order2:
    return 1
  return 0

def solution(numbers):
  # 1. 정수형 결합 후 비교를 위해 문자열 변환
  str_numbers = list(map(str,numbers))
  # 2. 커스텀 sort 진행
  str_numbers.sort(key=cmp_to_key(compare))
  if str_numbers[0] == "0":
      return "0"
    # 정렬된 문자열을 이어 붙여 결과를 반환합니다.
  return "".join(str_numbers)


print(solution([3,30,34,5,9]))