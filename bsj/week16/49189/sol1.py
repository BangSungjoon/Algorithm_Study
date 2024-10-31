# 가장 먼 노드
from collections import deque
def solution(n, edge):
    arr = set()
    # 인접 리스트 만들기
    adj_l = [[] for _ in range(n+1)]
    for e in edge:
        adj_l[e[0]].append(e[1])
        adj_l[e[1]].append(e[0])

    # node visited 만들기
    visited = [-1]*(n+1)
    visited[1] = 0

    # bfs로 만들기
    q = deque()
    for i in range(len(adj_l[1])):
        visited[adj_l[1][i]] = 1
        q.append(adj_l[1][i])
    while q:
        node = q.popleft()

        for k in adj_l[node]:
            if visited[k] == -1:
                visited[k] = visited[node]+1
                q.append(k)
    answer = 0
    for v in visited:
        if v == max(visited):
            answer += 1
    return answer