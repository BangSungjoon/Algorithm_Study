# [백준] 수들의 합 2
n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

for i in range(n):
    num = a[i]
    if num == m:
        answer += 1
        continue
    elif num < m:
        idx = i+1
        while num < m and idx < n:
            num += a[idx]
            idx += 1
            if num == m:
                answer += 1

print(answer)