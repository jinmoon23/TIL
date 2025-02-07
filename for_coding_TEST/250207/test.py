# import sys
# sys.stdin = open('input.txt')
# from itertools import combinations, permutations
# x=[[1,2],[3,5],[2,4,7]]

# x.sort(key=lambda x:(x[1]))

# print(x)

# print(list(combinations([0,1,2,4,2], 2)))
# print(list(permutations([0,1,2,4,2], 2)))
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = list(zip(*a))[2]
print(b)