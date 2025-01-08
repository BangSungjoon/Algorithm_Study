# PROGRAMMERS 피로도
# 87946
def solution(k, dungeons):
    answer = 0                      # 최대 클리어 횟수
    visited = [0] * len(dungeons)   # 던전 방명록

    def dfs(hp, count):
        nonlocal answer
        # 최대 클리어 횟수 갱신
        answer = max(answer, count)

        # 모든 던전 탐색
        for i in range(len(dungeons)):
            # 방문하지 않았고, 체력이 최소 요구치 이상인 경우만 진행
            if not visited[i] and hp >= dungeons[i][0]:
                visited[i] = 1  # 방문
                dfs(hp - dungeons[i][1], count + 1)  # 체력 소모 후 다음 탐색
                visited[i] = 0  # 취소

    dfs(k, 0)
    return answer
