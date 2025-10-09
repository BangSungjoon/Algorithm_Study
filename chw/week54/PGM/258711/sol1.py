def solution(edges):
    answer = []

    max_node = 0
    for u, v in edges:
        max_node = max(max_node, u, v)

    nodes = [[] for _ in range(max_node + 1)]

    for edge in edges:
        nodes[edge[0]].append(edge[1])

    # 생성 정점 찾기
    for idx, node in enumerate(nodes):
        if len(node) >= 2:
            for i in range(1, len(nodes)):
                if idx in nodes[i]:
                    break
            else:
                answer.append(idx)
                break

    # 각 그래프가 몇 개 있는지 판별
    graphs = [0] * 3  # 도넛, 막대, 8자

    for start in nodes[answer[0]]:
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

    return answer + graphs