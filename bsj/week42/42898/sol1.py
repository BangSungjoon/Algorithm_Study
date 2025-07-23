def solution(m, n, puddles):
    puddle_set = set((x, y) for x, y in puddles)
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                # 집이면 pass 합니더
                continue
            if (j, i) in puddle_set:
                # 물웅덩이일 경우도 pass
                continue
            left = j - 1
            up = i - 1
            dp[i][j] = dp[i][left] + dp[up][j]
    answer = dp[n][m] % 1000000007
    return answer