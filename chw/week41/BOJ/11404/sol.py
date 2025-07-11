import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
info = [list(map(int, input().split())) for _ in range(m)] # 시작, 도착, 비용

bus = [[0] * n for _ in range(n)]

for data in info:
    start = data[0] - 1
    end = data[1] - 1
    cost = data[2]

    if bus[start][end]:
        bus[start][end] = min(bus[start][end], cost)
    else:
        bus[start][end] = cost

for i in range(n):
    for j in range(n):
        start = i
        end = j

        if start == end:
            continue

        min_cost = 100001
        possible = []  # end에 도착하는 모든 버스(출발, 도착, 비용)
        for k in range(n):
            if bus[k][end]:
                possible.append((k, end, bus[k][end]))

        for p in possible:
            if p[0] == start:
                min_cost = min(min_cost, p[2])
                continue

            stack = [p]
            visited = [[0] * n for _ in range(n)]
            visited[p[0]][p[1]] = 1

            while stack:
                s, e, c = stack.pop()

                if s == start:
                    min_cost = min(min_cost, c)

                if c > min_cost:
                    continue

                for x in range(n):
                    if bus[x][s] and visited[x][s] == 0:
                        stack.append((x, s, c+bus[x][s]))
                        visited[x][s] = 1

        bus[i][j] = min_cost

for b in bus:
    print(*b)