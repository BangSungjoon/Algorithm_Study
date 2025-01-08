# info: 어피치의 점수 배열
# ryan: 라이언의 점수 배열

# 라이언과 어피치의 점수를 계산하고, 점수 차이를 반환하는 함수.
def calculate_score(info, ryan):
    rscore, ascore = 0, 0  # 각각 라이언과 어피치의 총 점수를 저장
    for i in range(11):  # 0점부터 10점까지 순회
        if ryan[i] > info[i]:  # 라이언이 더 많이 쏜 경우, 점수를 라이언에게 추가
            rscore += 10 - i
        elif info[i] > 0:  # 어피치가 점수를 가져가는 경우
            ascore += 10 - i
    return rscore - ascore  # 점수 차이를 반환


# n: 남은 화살 수
# idx: 현재 점수 구간(0~10)
# ryan: 현재 라이언의 점수 배열
# best_ryan: 최적의 라이언 점수 배열 (리스트로 참조 전달)
# max_diff: 최대 점수 차 (리스트로 참조 전달)



# DFS(깊이 우선 탐색)를 이용하여 가능한 모든 점수 조합을 탐색.
def dfs(n, idx, ryan, info, best_ryan, max_diff):

    # 종료 조건: 모든 점수대를 탐색했거나 화살을 모두 소진한 경우
    if idx == 11 or n == 0:
        ryan[10] += n  # 남은 화살은 0점 구간에 모두 추가
        diff = calculate_score(info, ryan)  # 점수 차이를 계산
        if diff > max_diff[0]:  # 점수 차이가 현재 최대 점수 차보다 큰 경우 갱신
            max_diff[0] = diff
            best_ryan[0] = ryan[:]  # 최적 배열 업데이트
        elif diff == max_diff[0]:  # 점수 차이가 같다면, 더 낮은 점수를 우선으로 비교
            if ryan[::-1] > best_ryan[0][::-1]:  # 배열을 뒤집어 비교(낮은 점수 구간부터 순차적으로 값을 비교)
                best_ryan[0] = ryan[:]
        ryan[10] -= n  # 0점에 추가했던 화살을 복구 (다른 경우를 위한 상태 복구)
        return

    # 어피치보다 1발 더 쏘는 경우
    if n > info[idx]:  # 화살이 충분할 때만 가능
        ryan[idx] = info[idx] + 1  # 어피치보다 1개 더 쏘기
        dfs(n - ryan[idx], idx + 1, ryan, info, best_ryan, max_diff)  # 화살 소모 후 다음 구간 탐색
        ryan[idx] = 0  # 상태 복구 (다른 경우를 위해 초기화)

    # 현재 점수대를 포기하는 경우
    dfs(n, idx + 1, ryan, info, best_ryan, max_diff)  # 화살 소모 없이 다음 구간 탐색


def solution(n, info):
    best_ryan = [[0] * 11]  # 최적의 라이언 점수 배열을 저장하는 리스트
    max_diff = [-1]  # 최대 점수 차이를 저장하는 리스트
    dfs(n, 0, [0] * 11, info, best_ryan, max_diff)  # DFS 탐색 시작
    return best_ryan[0] if max_diff[0] > 0 else [-1]  # 최대 점수 차가 0보다 크면 최적 배열 반환, 아니면 [-1]




