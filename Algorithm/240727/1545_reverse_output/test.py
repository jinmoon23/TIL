t = int(input())

def reverse_output(n):
    if n == 0:
        return 0
    else:
        return str(n) +' '+str(reverse_output(n-1))

print(reverse_output(t))