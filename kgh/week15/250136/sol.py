'''
아이디어 !!

bfs로 탐색

1. X축 길이의 빈 배열 준비. 각 열에서 채취 가능한 석유량 기록
2. 석유가 있으면, 석유 양은 카운트. 해당 위치는 큐에서 제거
3. 석유의 x축 위치를 기록해서 x축에서 시작~종료 위치 기록
4 .석유 탐색이 종료되면 빈 배열에, 석유의 개수를 시작~종류 위치에 추가
5. 최대 석유량 계산
'''

from collections import deque

def solution(land):
    # land의 세로, 가로 길이
    n, m = len(land), len(land[0])
    
    # 열 별 뽑을 수 있는 석유의 양
    oil_counts = [0] * m

    # visited 배열 생성
    visited = [[0] * m for _ in range(n)]
    
    def bfs(x, y):
        # 큐 초기화, 시작 위치 설정
        queue = deque([(x, y)])
        # 시작 위치 방문 체크
        visited[x][y] = 1
        # 현재 석유 덩어리 크기
        oil_size = 1
        
        # 현재 위치(y)에서부터 시작해서 석유 덩어리가 차지하는 가로로 확장해나갈라고
        min_col, max_col = y, y  # 덩어리가 걸치는 열 시작과 끝 기록
        
        while queue:
            # 현재 위치 꺼냄
            cx, cy = queue.popleft()
            # 델타 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                
                # 범위 안에 있고, 석유가 있으며, 방문하지 않은 경우
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0:
                    # 방문 체크, 큐에 ㅋ추가
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # 석유크기 += 1
                    oil_size += 1
                    # 현재 열의 최소, 최대 위치를 업데이트
                    min_col, max_col = min(min_col, ny), max(max_col, ny)
        
        # 시작~종료 열 위치에 석유량 누적
        # 각 col 열 위치에 석유 덩어리 크기 (oil_size)를 더해줌
        for col in range(min_col, max_col + 1):
            oil_counts[col] += oil_size

    # 각 위치를 탐색하며 석유 덩어리 찾기
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)

    # 가장 많은 석유량을 구함
    return max(oil_counts)