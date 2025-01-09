def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX

def solution(n, computers):
    parent = list(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(parent, i, j)
    
    return len(set(find(parent, i) for i in range(n)))
