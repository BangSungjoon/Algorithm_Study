def power(a, b, c):
    if b == 0:
        return 1

    x = power(a, b//2, c)

    if b % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c


A, B, C = map(int, input().split())
print(power(A, B, C))