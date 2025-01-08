# n * m 행렬 벗어나거나 벽일때는 처리X
# 방문할때마다 1기록, 이걸 다시 새출발점으로 사용할 수 있도록 큐리스트에 추가
# 각 위치까지의 최단 경로 길이를 maps 배열에 기록
# 0 벽있는 자리 1:벽없는자리

def solution(maps):
    answer = -1   # 기본값으로 -1 설정  
    n = len(maps)     # n은 행
    m = len(maps[0])  # m은 열
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0] * m for _ in range(n)]  # 방문기록 리스트
    queue = [(0,0)]  # 큐 리스트에  (0,0) 담아놓고 시작
    visited[0][0] = 1

    while queue:
        x, y = queue.pop(0)  
        for i in range(4):
            ni = x + dx[i]
            nj = y + dy[i]
            if 0 <= ni < n and 0 <= nj < m:
                if maps[ni][nj] == 1 and visited[ni][nj] == 0:  # 벽이 아니고, 방문한적이 없을때
                    queue.append((ni,nj))          # 큐리스트에 추가
                    visited[ni][nj] = 1            # 방문기록
                    maps[ni][nj] = maps[x][y] + 1
                    # maps[x][y]는 현재위치인 [x][y]까지 오는데 필요한 이동 횟수
                    # maps[ni][nj] = maps[x][y] + 1은 현재위치까지의 이동 횟수에 1을 더해줌으로써 새로운 위치[ni][nj]까지의 이동 횟수 계산하고
                    # 계산된 이동 횟수를 새로운 위치 (ni, nj)에 저장.
                    # 즉, 각 위치까지의 최단 경로 길이를 maps 배열에 기록

    if visited[n-1][m-1] != 0: # 우하단 상대진영에 방문했을경우에는 maps[n-1][m-1]의 값이 최단 경로의 길이 
        answer = maps[n-1][m-1]                

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) 