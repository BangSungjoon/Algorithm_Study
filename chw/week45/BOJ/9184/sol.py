arr = []

while True:
    x, y, z = map(int, input().split())

    if x == -1 and y == -1 and z == -1:
        break

    arr.append((x, y, z))

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def top_down_dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return top_down_dp(20, 20, 20)

    # 메모이제이션
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = top_down_dp(a, b, c - 1) + top_down_dp(a, b - 1, c - 1) - top_down_dp(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = top_down_dp(a-1, b, c) + top_down_dp(a-1, b-1, c) + top_down_dp(a-1, b, c-1) - top_down_dp(a-1, b-1, c-1)
    return dp[a][b][c]

for a, b, c in arr:
    ans = top_down_dp(a, b, c)

    print(f'w({a}, {b}, {c}) = {ans}')

