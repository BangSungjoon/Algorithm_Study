from collections import deque

def solution(n, vertex):
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # BFS 초기화
    queue = deque([1])  # 1번 노드에서 시작
    distances = [-1] * (n + 1)  # 거리를 저장할 리스트 (-1로 초기화)
    distances[1] = 0  # 1번 노드까지의 거리는 0
    max_distance = 0
    
    # BFS 수행
    while queue:
        # 하나 꺼내와
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # 아직 방문 안했다면
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
                # 최대 거리 갱신
                max_distance = max(max_distance, distances[neighbor])

    # 가장 먼 노드의 개수
    answer = sum(1 for distance in distances if distance == max_distance)
    
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))