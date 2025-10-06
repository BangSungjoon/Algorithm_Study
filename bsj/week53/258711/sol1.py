# [프로그래머스] 도넛과 막대 그래프
from collections import defaultdict

def solution(edges):
    # 생성한 정점의 번호 -> 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프와 연결된 정점
    # 도넛 모양 그래프나 막대 모양 그래프, 8자 모양 그래프의 수 합은 2개 이상
    in_dict = defaultdict(int)  # node별 들어온 간선의 수
    out_dict = defaultdict(int) # node별 나간 간선의 수
    nodes = set()
    
    for edge in edges:
        a, b = edge
        in_dict[b] += 1     # b노드로 하나 들어옴
        out_dict[a] += 1    # a노드에서 하나 나감
        nodes.add(a)
        nodes.add(b)
    created_node = 0
    for node in nodes:
        if out_dict[node] >= 2 and in_dict[node] == 0:
            created_node = node
            # answer[0] = node
            break
    # 막대 모양 그래프의 특징은 들어오는 간선은 하나이상이면서 나가는 간선은 없는 노드가 존재한다는 것이다.
    # 8자 모양 그래프의 특징은 들어오는 간선이 2개이상이면서 나가는 간선은 2개인 노드가 존재한다는 것이다.
    stick = 0
    eight = 0
    for node in nodes:
        if node == created_node:
            continue
        elif in_dict[node] >= 1 and out_dict[node] == 0:
            stick += 1
        elif in_dict[node] >= 2 and out_dict[node] == 2:
            eight += 1
    doughnut = out_dict[created_node] - stick - eight
    
    return [created_node, doughnut, stick, eight]