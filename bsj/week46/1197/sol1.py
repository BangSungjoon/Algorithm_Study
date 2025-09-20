# [백준] 최소 스패닝 트리
v, e = map(int, input().split())
adj_l = [[] for _ in range(v+1)]
arr = []

for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])

# 간선을 가중치 오름차순으로 정렬
arr.sort()

# union-find
parent = [i for i in range(v+1)]
rank = [0] * (v+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # root a, root b
    ra, rb = find(x), find(y)
    if ra == rb:        # 부모가 같다면
        return False    # 이미 같은 집합(사이클이 발생한다)
    # rank가 낮은 트리를 높은 트리에 붙이기
    if rank[ra] < rank[rb]:
        # ra의 rank가 rb보다 낮다면 rb에 종속
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        # ra와 rb의 rank가 같다면 -> 두 집합의 높이가 같음
        parent[rb] = ra     # rb 집합을 ra 집합 밑으로 붙임
        rank[ra] += 1       # ra의 높이가 한 단계 커짐
    return True

# 사이클을 만들지 않는 간선만 채택
answer = 0
cnt = 0
for c, a, b in arr:
    if union(a, b):
        answer += c
        cnt += 1
        if cnt == v - 1:
            break

print(answer)