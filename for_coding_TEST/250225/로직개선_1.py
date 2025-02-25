def solution(n, arr1, arr2):
  result = []
# 각 숫자의 이진 문자열을 n자리로 맞춘 후 각 자리를 비교하여 결과를 생성합니다.
  for num1, num2 in zip(arr1, arr2):
# zfill을 사용하여 왼쪽에 0을 채워 n자리 이진 문자열 생성
    row1 = bin(num1)[2:].zfill(n)
    row2 = bin(num2)[2:].zfill(n)
# 두 문자열의 각 자리를 비교해 하나라도 '1'이면 '#' 아니면 ' '로 변환
    row = ''.join('#' if c1 == '1' or c2 == '1' else ' ' for c1, c2 in zip(row1, row2))
    result.append(row)
  return result

print(solution(5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))