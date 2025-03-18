n, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(m+1)]
list = [[0,0]]

# dp[챕터][일수]
# if : j < 각 챕터 당 읽는데 소요되는 일수
# -> dp[i-1][j] 이전 챕터 페이지 값이 최댓값


for _ in range(m) :
  a, b = map(int, input().split())
  list.append([a,b])

# 정렬해주기(숫자를 비교해야하니까) 일수 기준으로 오름차순
list = sorted(list)

for i in range(1, m+1) :
  for j in range(1, n+1) :
    day, page = list[i][0], list[i][1] #day는 현재 챕터를 읽는 데 필요한 일수, page는 현재 챕터의 페이지 수
    if j < day :
      dp[i][j] = dp[i-1][j]
    else :
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)

print(dp[m][n])



# https://blog.naver.com/ej_0109/222765183071