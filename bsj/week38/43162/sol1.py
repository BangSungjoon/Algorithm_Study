def dfs(com, visited, computers, n):
    visited[com] = 1
    
    for j in range(n):
        if j == com:
            continue
        if computers[com][j] == 1 and visited[j] == 0:
            dfs(j, visited, computers, n)

def solution(n, computers):
    visited = [0]*n
    answer = 0
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, computers, n)
            answer += 1
    return answer