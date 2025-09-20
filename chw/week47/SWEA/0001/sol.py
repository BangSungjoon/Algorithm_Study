from heapq import heappush, heappop
from itertools import permutations

T = int(input())    # 테스트 케이스

# 최단 경로 찾기
def dijkstra(start):
    distance = [[1e9, []] for _ in range(n+1)]     # (최단 거리, 최단 경로) 저장

    q = []
    heappush(q, (0, start))
    distance[start][0] = 0

    while q:
        dist, current = heappop(q)  # 최단 거리의 노드 꺼내기

        # 이미 더 짧은 경로 찾았으면 무시
        if distance[current][0] < dist:
            continue

        # 현재 위치와 연결된 노드 탐색
        for next_node in graph[current]:
            node_b, r, c = next_node

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 기록된 거보다 짧으면 갱신
            cost = dist + r

            if cost < distance[node_b][0]:
                distance[node_b][0] = cost
                distance[node_b][1] = distance[current][1] + [node_b]

                for i in range(2, len(distance[node_b])):
                    distance[node_b][i] = []

                heappush(q, (cost, node_b))

            elif cost == distance[node_b][0]:
                distance[node_b].append(distance[current][1] + [node_b])

                heappush(q, (cost, node_b))

    for idx, d in enumerate(distance):
        for x in range(1, len(d)):
            d[x].append(idx)

    return distance


for t in range(T):
    ans = []

    n, m = map(int, input().split())  # n 노드 개수, m 전선 개수
    arr = [list(map(int, input().split())) for _ in range(m)]  # 전선 정보
    k = int(input())
    target = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]    # 노드A(인덱스)에서 갈 수 있는 간선 정보

    for info in arr:
        node_A = info[0]
        node_B = info[1]
        resistance = info[2]
        channel = info[3]

        graph[node_A].append((node_B, resistance, channel))
        graph[node_B].append((node_A, resistance, channel))

    # 각 노드에서 다른 노드까지 최단 경로를 미리 계산
    distance_map = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        distance = dijkstra(i)
        distance_map[i] = distance

    possible = permutations(range(1, n+1), 2)   # 가능한 출발-도착 노드 쌍
    # possible = [(4,5)]
    for p in possible:
        start = p[0]
        end = p[1]

        # start 부터 인접한 노드로 이동하면서 목표 채널 기록과 같은지 확인, 같으면 진행
        success = True

        now = start
        path = []
        for j in range(k):
            if not success:
                break

            for information in graph[now]:
                record = 0

                # 최단 경로에 포함되는지 여부 판단
                for i in range(1, len(distance_map[now][end])):
                    if information[0] in distance_map[now][end][i]:
                        record = information[2]

                        if record == target[j]:
                            break
                    else:
                        record = -information[2]

                        if record == target[j]:
                            break

                # 목표 경로와 같다면 path에 넣고 다음 경로 찾기
                if record == target[j]:
                    path.append(record)
                    now = information[0]
                    break
                else:
                    continue

            # 일치하는 게 하나도 없으면 해당 출발-노드 쌍 패스
            else:
                success = False

        # 실패한 쌍이면 다음 쌍 보기
        if not success:
            continue
        elif path == target:
            ans.append((start, end))

    print(f'#{t+1}')
    for a in ans:
        print(*a)