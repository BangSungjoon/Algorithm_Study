#백백백트래킹


def solution(k, dungeon):
    def dfs(k, dungeon, visited, count):
        nonlocal max_count
        # 현재까지 탐험한 던전 수가 최대값보다 크면 최대값 갱신
        max_count = max(max_count, count)
        
        # 모든 던전을 순회
        for i in range(len(dungeon)):
            # 아직 방문하지 않았고, 현재 피로도로 탐험 가능한 던전이라면
            if not visited[i] and k >= dungeon[i][0]:
                visited[i] = True  # 던전 방문 처리
                # 피로도를 소모하고 다음 던전으로 재귀 호출
                dfs(k - dungeon[i][1], dungeon, visited, count + 1)
                visited[i] = False  # 백트래킹: 방문 처리 취소
    
    max_count = 0  # 최대 탐험 가능 던전 수 초기화
    visited = [False] * len(dungeon)  # 던전 방문 여부 리스트 초기화
    dfs(k, dungeon, visited, 0)  # DFS 시작
    return max_count
