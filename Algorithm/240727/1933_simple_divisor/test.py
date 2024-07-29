N = int(input())

def find_divisor(n):
    result = ''
    for i in range(1,n+1):
        if n % i == 0:
            result += str(i) + ' '
    return result

print(find_divisor(N))