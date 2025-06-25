def solution(n, computers):
    visited = [0] * n
    cnt = 0
    for i in range(len(computers)):
        # 방문한 적 없으면 네트워크 +1, 연결된 네트워크 살펴보기
        q = []
        if visited[i] == 0:
            cnt += 1
            for idx, com in enumerate(computers[i]):
                if idx != i and com == 1:
                    q.append((i, idx))

        while q:
            start, next = q.pop()
            visited[start] = 1
            visited[next] = 1
            for idx, com in enumerate(computers[next]):
                if idx != start and idx != next and com == 1 and visited[idx] == 0:
                    visited[idx] = 1
                    q.append((next, idx))

    return cnt