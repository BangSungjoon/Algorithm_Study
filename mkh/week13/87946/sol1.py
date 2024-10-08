from collections import deque


def solution(k, dungeons):
    q = deque()
    n = len(dungeons)
    for i in range(n):
        if k >= dungeons[i][0]:
            q.append((k-dungeons[i][1], [i]))

    max_len = 0

    while q:
        piro, visited = q.popleft()
        if max_len < len(visited):
            max_len = len(visited)
        for i in range(n):
            if i not in visited and piro >= dungeons[i][0]:
                q.append((piro-dungeons[i][1], visited+[i]))

    return max_len


print(solution(80, [[80,20],[50,40],[30,10]]))
