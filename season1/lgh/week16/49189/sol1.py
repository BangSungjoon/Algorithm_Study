# 가장 먼 노드
# 1번 노드로부터 가장 먼 노드들의 개수 구하기

def solution(n, edge):
    graph = [[] for _ in range(n+1)] # 1~n번까지 각 노드의 빈리스트 생성
    visited = [0] * (n + 1) # 방문여부와 거리를 기록할 리스트

    for node in edge:
        a, b = node[0], node[1] # 간선의 양 끝점 
        graph[a].append(b)  # 양방향 그래프이므로, 서로 리스트에 추가
        graph[b].append(a)


    q = [] 
    q.append(1) # 시작노드 큐에 추가
    visited[1] = 1 # 시작노드 방문처리, 거리 1

    while q:
        x = q.pop(0) # 큐에서 현재 노드 추출
        for i in graph[x]: # 현재 노드와 연결된 모든 노드 탐색
            if not visited[i]: # 방문하지 않은 노드의 경우
                visited[i] = visited[x] + 1 # 현재 노드의 거리 + 1         
                q.append(i)

    max_value = max(visited) # 방문한 노드들 중 최대거리 찾기
    answer = visited.count(max_value) # 개수 세기           
    return answer

n = 6 
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))