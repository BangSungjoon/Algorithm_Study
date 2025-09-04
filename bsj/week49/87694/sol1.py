from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[0]*101 for _ in range(101)]
    
    # 모든 사각형을 1로 표현
    for left_x, left_y, right_x, right_y in rectangle:
        left_x, left_y, right_x, right_y = left_x*2, left_y*2, right_x*2, right_y*2
        for y in range(left_y, right_y+1):
            for x in range(left_x, right_x+1):
                arr[y][x] = 1
    # 사각형 내부를 0으로 만들어 테두리만 남기기
    for left_x, left_y, right_x, right_y in rectangle:
        left_x, left_y, right_x, right_y = left_x*2, left_y*2, right_x*2, right_y*2
        for y in range(left_y+1, right_y):
            for x in range(left_x+1, right_x):
                arr[y][x] = 0
    # bfs
    cx, cy = characterX*2, characterY*2
    ix, iy = itemX*2, itemY*2
    
    q = deque([(cx, cy, 0)])
    visited = [[0]*101 for _ in range(101)]
    visited[cy][cx] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y, distance = q.popleft()
        if (x, y) == (ix, iy):
            answer = distance // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 101 and 0 <= ny < 101 and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append((nx, ny, distance+1))
        
    return answer