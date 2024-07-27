# 2027, 대각선 출력

## 풀이 과정
1. list -> str(join)
2. try except 사용하지 않으면 index error 발생 -> 5번째 인덱스는 없기 때문. 하지만 range(len(dummy_list)-1) 하면 원하는 출력이 완성되지 않음
