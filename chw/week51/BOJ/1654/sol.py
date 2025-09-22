K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

max_len = max(lines)
min_len = 1
ans = 0

while min_len <= max_len:
    target_len = (max_len + min_len) // 2

    cnt = 0

    for line in lines:
        cnt += line // target_len

    # N개 만들면 성공
    if cnt >= N:
        ans = target_len
        min_len = target_len + 1
    # N개 보다 적게 만들면 최대 값을 현재 값으로
    else:
        max_len = target_len - 1

print(ans)