N = int(input())    # 노드의 갯수
info = [list(map(int, input().split())) for _ in range(N-1)]    # 노드 간 연결 정보

tree = [[] for _ in range(N+1)]     # idx 노드에 연결된 노드들을 기록
res = [0] * (N+1)   # 각 노드의 부모 노드를 기록

for link in info:
    a = link[0]
    b = link[1]
    tree[a].append(b)
    tree[b].append(a)

for i in range(1, N+1):
    # 루트 노드가 부모인 노드들의 부모 기록
    if i == 1:
        for node in tree[1]:
            res[node] = 1

    # 부모가 기록 되어 있지 않으면
    if not res[i]:
        # 연결된 노드를 확인해서 부모가 있으면 내가 그 노드의 자식 노드
        for node in tree[i]:
            if res[node]:
                res[i] = node
            else:
                continue

for j in range(2, N+1):
    print(res[j])