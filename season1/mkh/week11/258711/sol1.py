import sys
sys.setrecursionlimit(1000000)


def solution(edges):
    ans = [0]*4
    leng = max([max(x[0], x[1]) for x in edges])+1
    going_list = [[] for _ in range(leng)]
    coming_list = [[] for _ in range(leng)]
    # 가장 큰 노드 번호를 기준으로 인접리스트 생성
    for s, e in edges:
        going_list[s].append(e)
        coming_list[e].append(s)
    # 인접리스트 채우기
    inserted_edge = 0
    max_len = 0
    for i in range(leng):
        if max_len < len(going_list[i]) and not coming_list[i]:
            max_len = len(going_list[i])
            inserted_edge = i
    # 인접리스트에서 나가는 노드 개수가 제일 많으면서 들어오는 노드개수가 없는 경우 삽입된 노드임
    ans[0] = inserted_edge

    def dfs(curr, start, flag=False):
        nonlocal ans
        if len(going_list[curr])>1:     # 나가는 노드가 2개 이상이면 8자 모양
            ans[3] += 1
        elif curr == start and flag:    # 현재노드랑 시작 노드랑 같으면 도넛 모양
            ans[1] += 1
        elif not going_list[curr]:      # 나가는 노드가 없는 경우 막대 모양
            ans[2] += 1
        else:                           # 아니라면 다음 노드로 진행~!
            dfs(going_list[curr][0], start, True)
    
    # 삽입된 노드에서 나가는 노드들이 루프의 일부이므로 그 노드들부터 시작함
    for loop_node in going_list[inserted_edge]:
        dfs(loop_node,loop_node)

    return ans