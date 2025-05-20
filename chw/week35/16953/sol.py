A, B = list(map(int, input().split()))
ans = 1e9

def solution(num, cnt):
    global ans

    if num == B:
        ans = min(ans, cnt)
        return

    if num > B:
        return

    solution(num * 2, cnt + 1)
    solution(num * 10 + 1, cnt + 1)

solution(A, 0)

if ans == 1e9:
    print(-1)
else:
    print(ans+1)