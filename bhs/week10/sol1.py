from collections import deque


def bfs_solution(maps, start, end):
    n, m = len(maps), len(maps[0])
    queue = deque([(start, [start])])  # (현재 위치, 경로)
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # 목표 지점에 도달하면 경로 반환

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                next_pos = (nx, ny)
                queue.append((next_pos, path + [next_pos]))
                visited.add(next_pos)

    return None  # 경로를 찾지 못한 경우

def solution(maps):
    n, m = len(maps), len(maps[0])
    start = (0, 0)
    end = (n - 1, m - 1)

    path = bfs_solution(maps, start, end)

    if path:
        return len(path)-1
    else:
        return -1
