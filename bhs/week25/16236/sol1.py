from collections import deque

N = int(input())
foodmap = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

pos = []
for i in range(N):
    for j in range(N):
        if foodmap[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0

# 가까운 먹이를 찾는 탐색 문제이기 때문에 `BFS`를 생각해 볼 수 있다.
# BFS를 사용할 시 입력으로는 현재 아기 상어의 위치를 생각할 수 있고,
# 출력으로는 후보를 리스트를 반환 해야한다.
def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x,y]])
    nominate = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ni, nj = i + dx[idx] , j + dy[idx]

            if 0 <= ni and ni < N and 0 <= nj and nj < N and visited[ni][nj] == 0:
				# 5. 간선은 상하 좌우지만 조건에 따라서 움직이기 때문에 조건을 상세하여야한다.
                if foodmap[x][y] > foodmap[ni][nj] and foodmap[ni][nj] != 0:
                    visited[ni][nj] =  visited[i][j] + 1
                    nominate.append((visited[ni][nj] - 1, ni, nj))
                elif foodmap[x][y] == foodmap[ni][nj]:
                    visited[ni][nj] =  visited[i][j] + 1
                    queue.append([ni,nj])
                elif foodmap[ni][nj] == 0:
                    visited[ni][nj] =  visited[i][j] + 1
                    queue.append([ni,nj])
                    
	# 6. 후보 리스트는 우선 순위가 있기 때문에 정렬을 사용할 수 있다.
    # return sorted(nominate, key = lambda x: (x[0], x[1], x[2]))

    sorted_nominate = sorted([(x[0], x[1], x[2], x) for x in nominate])
    return [item[3] for item in sorted_nominate]


i, j = pos
size = [2, 0]
# 8. 맨 앞의 후보만 먹고 위치 이동후 다시 BFS 해야한다
while True:
    foodmap[i][j] = size[0]
    nominate = deque(bfs(i,j))
    
    if not nominate:
        break
        
    # 7. 후보리스트가 나오면 맨 앞의 후보 먹이를 뽑아 그 위치로 이동한다.
    step, xx, yy = nominate.popleft()
    cnt += step
    size[1] += 1
    
	# 9. 몇 개를 먹었는지 몇 초간 이동했는지 체크해 줄 필요가 있다.
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    foodmap[i][j] = 0
    i, j = xx, yy
        
print(cnt)