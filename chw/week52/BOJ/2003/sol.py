N, M = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
cnt = 0
total = 0

for start in range(N):
    while total < M and end < N:
        total += nums[end]
        end += 1

    if total == M:
        cnt += 1

    total -= nums[start]

print(cnt)