import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 초기화: 무한대로 설정
INF = float('inf')
dist = [[INF] * n for _ in range(n)]

# 자기 자신으로 가는 거리는 0
for i in range(n):
    dist[i][i] = 0

# 직접 연결된 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1  # 0-based indexing
    b -= 1
    dist[a][b] = min(dist[a][b], c)  # 같은 경로 여러 개면 최솟값

# 플로이드-워셜 알고리즘
for k in range(n):  # 경유지
    for i in range(n):  # 시작점
        for j in range(n):  # 끝점
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 출력 (갈 수 없으면 0)
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()