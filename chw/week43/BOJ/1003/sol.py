import sys
input = sys.stdin.readline

T = int(input())

def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

f = [[] for _ in range(41)]
f[0] = [1, 0]
f[1] = [0, 1]
f[2] = [1, 1]

for i in range(3, 41):
    f[i] = [f[i-1][0] + f[i-2][0], f[i-1][1] + f[i-2][1]]

for _ in range(T):
    n = int(input())

    print(*f[n])