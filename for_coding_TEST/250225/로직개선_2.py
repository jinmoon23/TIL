def solution(n, arr1, arr2):
  result = []
  for a, b in zip(arr1, arr2):
# 비트 OR 연산을 통해 두 지도 정보를 통합
    merged = a | b
# n자리 이진 문자열로 변환하고, 1은 '#', 0은 ' '로 치환
    row = format(merged, '0{}b'.format(n)).replace('1', '#').replace('0', ' ')
    result.append(row)
  return result

print(solution(5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))