# DFS : 깊이 우선이므로 최단 경로를 찾을 때는 적합하지 않다. 우선 탐색된 경로가 최단경로임을 보장하지 않은 채 메모리를 남비
# BFS : 최단 경로 문제에 매우 적합. 항상 시작점에서 가까운 노드부터 차례대로 방문한다. 즉, 먼저 방문하는 노드들은 항상 더 적은 이동 횟수로 도달할 수 있는 노드들이다.

def solution(maps):
    # 지도의 행과 열의 개수
    n, m = len(maps), len(maps[0])
    # BFS를 위한 큐에 시작점 push
    queue = [(0, 0)]
    # 방문 체크 리스트
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1  # 시작점 방문 체크
    maps[0][0] = 1     # 거리 계산 이걸로 할거야. 시작점의 거리를 1로 설정

    # BFS 탐색
    while queue:
        x, y = queue.pop(0)  # 현재 위치
        # 델타 탐색 (상, 하, 좌, 우)
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy  # 다음 이동할 노드 계산
            if 0 <= nx < n and 0 <= ny < m:  # 다음 이동할 노드가 지도 범위 내 있는지
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:   # 아직 방문 안했고, 지도에서 길이면
                    queue.append((nx, ny))  # 큐에 추가
                    visited[nx][ny] = 1     # 방문 체크
                    maps[nx][ny] = maps[x][y] + 1  # 인접 노드의 거리 = 현재 노드의 거리 + 1
    # 도착 지점 행 n, 열 m -> 인덱스로는 -1씩
    if visited[n-1][m-1] != 0:  # 도착했으면
        return maps[n-1][m-1]   # 최단거리 반환
    else:  # 도착못하면
        return -1  # -1 반환
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1