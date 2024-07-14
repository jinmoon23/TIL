# 최초 코드
# a,b = map(int, input().split())
# A = False
# B = False
# if a == 1:
#     if b == 2:
#         A = False
#         B = True
#     else:
#         A = True
#         B = False
# if a == 2:
#     if b == 1:
#         A = True
#         B = False
#     else:
#         A = False
#         B = True
# if a == 3:
#     if b == 1:
#         A = False
#         B = True
#     else:
#         A = True
#         B = False

# if A == True:
#     print("A")
# else:
#     print("B")

# GPT에게 리팩토링을 맡긴 경우
a, b = map(int, input().split())

if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("A")
else:
    print("B")