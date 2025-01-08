from collections import deque
'''
x좌표, y좌표를 쭉 탐색하면서 갈 수 있는 곳들을 BFS로 탐색. 최소기록만 탐색하면 되니까.
몇 번 왔던간에 한 번 왔던 곳에서 다시 간다 해도 변화가 없으므로
visited는 좌표들만 기록해줘도 된다.
앞으로 갈 togo의 목록이 다 비워지는 경우 -1을 반환
'''

def solution(board):
    visited = set()
    togo = deque()
    h = len(board)
    w = len(board[0])
    answer = 0
    
    # 시작할 지점 R과 목표지점 G의 좌표 찾아서 할당해주기. 
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                togo.append((i, j, 0,))
            elif board[i][j] == 'G':
                t_y = i
                t_x = j
        
    # BFS 탐색 시작
    while togo:
        y, x, tries = togo.popleft()
        # 목표 지점에 도착했다면, 탐색을 종료
        if y == t_y and x == t_x:
            answer = tries
            break
        
        # 방문 표시
        
        # 지금 있는 곳 위쪽으로 탐색
        # y 가 제일 위에 있다면 위로 미끄러질 수 없으므로 판별할 필요 x
        i = y-1
        while i != -1:
            if board[i][x] == 'D':
                if (i+1, x) not in visited:
                    togo.append((i+1, x, tries+1))
                    visited.add((i+1,x))
                # if 안에서 break를 선언할 경우 돌을 뚫고 탐색하므로 if문 밖에서 break
                break
            i -= 1
        # 걸리는 곳이 없더라도 제일 위로 갈 수도 있으므로 확인
        else:
            if y != 0 and (0,x) not in visited:
                visited.add((0,x))
                togo.append((0, x, tries+1))
        # 지금 있는 곳 아래쪽으로 탐색
        i = y+1
        while i != h:
            if board[i][x] == 'D':
                if (i-1, x) not in visited:
                    togo.append((i-1, x, tries+1))
                    visited.add((i-1,x))
                break
            i += 1
        else:
            if y != h-1 and (h-1,x) not in visited:
                visited.add((h-1,x))
                togo.append((h-1, x, tries+1))
                
        # 지금 있는 곳 왼쪽으로 탐색
        i = x-1
        while i != -1:
            if board[y][i] == 'D':
                if (y, i+1) not in visited:
                    togo.append((y, i+1, tries+1))
                    visited.add((y,i+1))
                break
            i -= 1
        else:
            if x != 0 and (y,0) not in visited:
                togo.append((y, 0, tries+1))
                visited.add((y,0))
                
                
        # 지금 있는 곳 오른쪽으로 탐색
        i = x+1
        while i != w:
            if board[y][i] == 'D':
                if (y, i-1) not in visited:
                    visited.add((y,i-1))
                    togo.append((y, i-1, tries+1))
                break
            i += 1
        else:
            if x != w-1 and (y,w-1) not in visited:
                visited.add((y,w-1))
                togo.append((y, w-1, tries+1))
                    
    else: answer = -1
        
    
    return answer