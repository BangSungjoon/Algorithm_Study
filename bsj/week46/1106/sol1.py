# [백준] 호텔
# 다이나믹 프로그래밍을 사용해서 풀어보자
c, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [float('inf')]*(c+100) # idx는 고객, value는 최소 비용 c명을 넘은 범위에서 최소 금액이 발생할 수 있다.
dp[0] = 0 # 0명을 늘리려면 0원이 드니깐

for cost, cnt_people in arr:
    # 비용의 배수만큼 고객을 얻을 수 있는지 갱신
    for i in range(cnt_people, c+100):
        dp[i] = min(dp[i], dp[i-cnt_people]+cost)

print(min(dp[c:]))