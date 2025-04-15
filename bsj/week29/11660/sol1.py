# 구간 합 구하기 5
"""
점화식으로 어떻게 나눌 것인가?
-> (1, 1) 부터 (x2, y2)까지의 합 - 해당 하지 않는 부분 + 겹치는 부분
dp[x][y]는 1부터 (x, y)까지의 누적 합
"""
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # 현재 영역 + x축으로 한칸 전 누적합 + y축으로 한칸 전 누적합 - 겹치는 부분 누적합
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 1,1부터 x2,y2까지의 누적합 - 1,1부터 x1이전의 누적합 - 1,1부터 y1이전의 누적합 + 겹쳐서 더 빼진 부분
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(result)