import sys, copy
input = sys.stdin.readline

a, b = map(int, input().split())

count = 0
while b > a:
    if b % 10 == 1:
        b //= 10   # 10으로 나누어서 끝자리 1을 제거
    elif b % 2 == 0:
        b /= 2
    else :
        break
    count += 1

if a == b:
    print(count + 1)
else:
    print(-1)


    ## A를 B로 만드는 게 아니라 B를 A로 만드는 게 더 이득
