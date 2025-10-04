# [백준] 도시 분할 계획
def find_parent(x):
    # 부모 찾기
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    # 두 집합 합치기
    a, b = find_parent(x), find_parent(y)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 집의 개수 n, 길의 개수 m
n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

parents = [0]*(n+1)
for i in range(1, n+1):
    parents[i] = i

result = 0
max_cost = 0
for edge in edges:
    cost, a, b = edge

    # 부모가 다르다면 이미 한 집합이 아닌것이다
    if find_parent(a) != find_parent(b):
        # 이제 한 식구여
        union_parent(a, b)
        result += cost
        max_cost = max(max_cost, cost)

print(result - max_cost)