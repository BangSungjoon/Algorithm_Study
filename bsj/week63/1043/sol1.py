from collections import deque

N, M = map(int, input().split())

truth_info = list(map(int, input().split()))
truth_people = truth_info[1:]  # 진실 아는 사람들

# 그래프 노드 수: 사람 N명 + 파티 M개
# 파티 노드 인덱스: N+1 ~ N+M
graph = [[] for _ in range(N + M + 1)]

# 입력 받으며 사람-파티 연결
for party_idx in range(1, M + 1):
    data = list(map(int, input().split()))
    members = data[1:]
    party_node = N + party_idx

    for person in members:
        graph[person].append(party_node)
        graph[party_node].append(person)

# BFS: 진실이 도달 가능한 노드 찾기
visited = [False] * (N + M + 1)
q = deque()

for p in truth_people:
    visited[p] = True
    q.append(p)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

# 진실이 도달한 파티(visited[party_node] == True)는 거짓말 불가
ans = 0
for party_idx in range(1, M + 1):
    party_node = N + party_idx
    if not visited[party_node]:
        ans += 1

print(ans)