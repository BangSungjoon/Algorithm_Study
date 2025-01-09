def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]  # visited 배열
    visited[0][0] = 1
    min_num = 1e9
    # BFS
    q = [(0, 0)]
    ans = False
    level = 1
    while q:
        temp = []
        while q:
            r, c = q.pop(0)
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    temp.append((nr, nc))
                if nr == n - 1 and nc == m - 1:
                    ans = True
                    break
            if ans == True:
                break

        level += 1
        q = temp

        if ans == True:
            break

    if ans == False:
        answer = -1
    else:
        answer = level

    return answer