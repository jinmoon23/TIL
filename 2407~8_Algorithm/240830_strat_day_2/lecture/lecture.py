'''
0x4A3
25(10)
'''
# print(1)
# print(1 << 1, bin(1<<1))
# print(1 << 2, bin(1<<2))
# print(1 << 3, bin(1<<3))
# print(1 << 4, bin(1<<4))
# print(1)

# arr = [1,2,3,4]
#
# for i in range(1 << len(arr)):
#     print(i, end=' ')
# print()

# i & (1 << N) : N번째 비트가 0인지 1인지 알 수 있다.
# i 의 의미 : i번째 부분집합
# for i in range(1 << len(arr)):
#     for idx in range((len(arr))):
#         if i & (1 << idx):
#             print(arr[idx], end=' ')
#     print()

print(bin(4))
print(bin(~4))
print(~4)

t = 0.1
print(f'{t:.2f}')