def solution(edges):
    max_node = 0
    for u, v in edges:
        max_node = max(max_node, u, v)

    nodes = [[] for _ in range(max_node + 1)]
    out_degree = [0] * (max_node + 1)
    in_degree = [0] * (max_node + 1)

    for u, v in edges:
        out_degree[u] += 1
        in_degree[v] += 1
        nodes[u].append(v)

    # 생성 정점 찾기
    created_node = 0
    for i in range(1, max_node + 1):
        # 진출 2 이상, 진입 0인 노드가 생성된 정점
        if out_degree[i] >= 2 and in_degree[i] == 0:
            created_node = i
            break

    # 각 그래프가 몇 개 있는지 판별
    graphs = [0] * 3  # 도넛, 막대, 8자

    for start in nodes[created_node]:
        current = start

        turn = 0

        while True:
            turn += 1

            # 막대 그래프는 나가는 간선이 없는 노드가 존재
            # 8자 그래프는 중앙점이 나가는 간선이 2개
            if len(nodes[current]) == 0:
                graphs[1] += 1
                break
            elif len(nodes[current]) >= 2:
                graphs[2] += 1
                break

            # 만약 시작점으로 돌아왔으면 도넛 그래프
            if current == start and turn > 1:
                graphs[0] += 1
                break

            current = nodes[current][0]

    answer = [created_node] + graphs
    return answer