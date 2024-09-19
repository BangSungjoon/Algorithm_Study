# 정확성 O, 효율성 X
min_num = 1e9
def DFS(maps, r, c, cnt, n, m, visited):
    global min_num, ans
    copy_visited = [row[:] for row in visited]
    if r == n-1 and c == m-1:
        min_num = min(cnt, min_num)
        return
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr = r+dr
        nc = c+dc
        if 0<=nr<n and 0<=nc<m and maps[nr][nc] and not copy_visited[nr][nc]:
            copy_visited[nr][nc] = 1
            DFS(maps, nr, nc, cnt+1, n, m, copy_visited)

def solution(maps):
    # 캐릭터는 좌측 상단인 (1, 1) 위치 = (0, 0)
    # 상대방 진영은 우측 하단인 (n, m) 위치 = (n-1, m-1) -> n과 m을 알아야 함
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)] # visited 배열
    visited[0][0] = 1
    DFS(maps, 0, 0, 1, n, m, visited)
    if min_num == 1e9:
        answer = -1
    else:
        answer = min_num
    return answer