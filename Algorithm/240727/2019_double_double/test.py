t = int(input())

def double_double(n):
    result = ''
    for i in range(0,n+1):
        result += str(2**i) + ' '
    return result

print(double_double(t))