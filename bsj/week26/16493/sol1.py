# 최대 페이지 수
n, m = map(int, input().split())    # n: 대출 반납 일자, m: 챕터 수
arr = [[0, 0]]              # arr[i]는 [소요 일수, 페이지]
for _ in range(m):
    arr.append(list(map(int, input().split())))

# i번째 챕터까지 봤을 때, j의 날짜를 사용하여 얻을 수 있는 최대 페이지 수
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(n+1):
        if j - arr[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j - arr[i][0]] + arr[i][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[m][n])