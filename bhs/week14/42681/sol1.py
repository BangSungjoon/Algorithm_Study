섬 연결하기- 주석은 gpt의 도움을 받았습니다~

def find_parent(parent, x):      # 원소들이 속한 집합찾기
	    if parent[x] != x:         # 현재 원소 x의 부모다 자신이 아니라면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]             # 최종 부모를 반환


def solution(n, costs):
    costs.sort(key=lambda x: x[2])      # 비용순으로 간선 리스트를 오름차순으로 정렬
    
    parent = [i for i in range(n)]      # 각 원소의 부모를 자기 자신으로 초기화

    total_cost = 0                      # 최소비용

    for start, end, cost in costs:     # 정렬된 비용 리스트를 순회
        if find_parent(parent, start) != find_parent(parent, end):      # 사이클에 없니? - 시작 노드와 끝노드의 부모가 다르면
            total_cost += cost                                          # 추가
    
    return total_cost          # 최소 비용 반환
    
 # 테스트 케이스 2만 맞음.
 
 부모만? 바꾸어주기
 
