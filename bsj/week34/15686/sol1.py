# [백준] 치킨 배달
def dfs(idx, cnt):
    global result

    if cnt == m:
        # result와 비교하고 넘겨
        ans = 0

        for i in 집:
            거리 = float('inf')
            for j in range(치킨집_수):
                if visited[j]:
                    거리계산 = abs(i[0]-치킨[j][0])+abs(i[1]-치킨[j][1])
                    거리 = min(거리, 거리계산)
            ans += 거리
        result = min(ans, result)

        return

    for i in range(idx, 치킨집_수):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, cnt+1)
            visited[i] = 0

n, m = map(int, input().split())    # n은 도시의 크기, m은 폐업시키지 않을 치킨집 최대 개수
arr = [list(map(int, input().split())) for _ in range(n)]   # 0은 빈 칸, 1은 집, 2는 치킨집
result = float('inf')

집 = []
치킨 = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            집.append((i,j))
        elif arr[i][j] == 2:
            치킨.append((i,j))
치킨집_수 = len(치킨)
visited = [0]*치킨집_수
dfs(0, 0)
print(result)