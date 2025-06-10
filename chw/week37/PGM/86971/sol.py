from collections import deque

def solution(n, wires):
    ans = 1e9

    tree = [[] for _ in range(n + 1)]   # 인접 리스트에 트리 정보 기록

    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])

    def bfs(start, a, b, visited):
        q = deque([start])
        cnt = 1

        while q:
            node = q.popleft()
            if visited[node] == 0:
                # a와 b가 연결되어 있으면 건너뛰기
                for neighbor in tree[node]:
                    if node == a and neighbor == b:
                        continue
                    elif node == b and neighbor == a:
                        continue
                    else:
                        if visited[neighbor] == 0:
                            q.append(neighbor)
                            cnt += 1
                visited[node] = 1

        return cnt

    for w in wires:
        cnt = bfs(1, w[0], w[1], [0] * (n + 1))     # w[0]과 w[1]의 연결 끊기

        res = abs(cnt - (n - cnt))
        ans = min(ans, res)

    return ans