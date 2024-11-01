def dfs(computer, computers, visited):
    visited[computer] = True
    for i in range(len(computers)):
        if computers[computer][i] == 1 and not visited[i]:
            dfs(i, computers, visited)

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터라면
            dfs(i, computers, visited)  # 연결된 네트워크를 찾음
            answer += 1  # 새로운 네트워크 발견 시 개수 증가

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))