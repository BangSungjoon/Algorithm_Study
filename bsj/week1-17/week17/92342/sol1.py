# 프로그래머스 양궁대회
# 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏜다
# 0~10점이 있고 그 점수대에 가장 많은 화살을 맞춘 선수가 k점을 가져감
# 만약 맞춘 횟수가 같다면 어피치가 점수를 가져감 (k점만)
# 둘다 맞추지 않은 점수는 누구도 k점을 가져가지 않는다.
# 어피치가 다 쏜 상황, 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을
# 어느 점수에 맞춰야 할까?
def solution(n, info):
    # n: 라이언이 쏠 수 있는 화살 수
    # info: 어피치가 맞힌 과녁 점수, 10점부터 0점까지 순서대로
    answer = [-1]  # 최종 결과를 저장할 변수 (초기값: [-1])
    max_diff = 0  # 최대 점수 차이를 저장할 변수

    # DFS 함수 정의
    def dfs(idx, lion, arrows_left):
        nonlocal answer, max_diff

        # 기저 조건: 과녁의 끝(10점)을 넘어가거나 화살을 모두 소진한 경우
        if idx == 11 or arrows_left == 0:
            lion[10] += arrows_left  # 남은 화살은 0점에 배치
            apeach_score, lion_score = 0, 0

            # 점수 계산
            for i in range(11):
                if info[i] == 0 and lion[i] == 0:
                    continue  # 어피치와 라이언 모두 해당 점수를 못 맞춘 경우 제외
                if lion[i] > info[i]:
                    lion_score += 10 - i  # 라이언이 점수를 가져감
                else:
                    apeach_score += 10 - i  # 어피치가 점수를 가져감

            # 점수 차이가 더 크다면 결과 갱신
            diff = lion_score - apeach_score
            if diff > 0:  # 라이언이 어피치를 이긴 경우만 처리
                # 점수 차이가 최대일 때, 혹은 낮은 점수를 더 많이 맞힌 경우 갱신
                if diff > max_diff or (diff == max_diff and lion[::-1] > answer[::-1]):
                    max_diff = diff
                    answer = lion[:]
            lion[10] -= arrows_left  # 복원
            return

        # 현재 점수를 가져가는 경우
        if arrows_left > info[idx]:  # 남은 화살로 점수를 가져갈 수 있는 경우
            lion[idx] = info[idx] + 1  # 어피치보다 1발 더 쏘기
            dfs(idx + 1, lion, arrows_left - lion[idx])  # 다음 점수로 이동
            lion[idx] = 0  # 복원

        # 현재 점수를 가져가지 않는 경우
        dfs(idx + 1, lion, arrows_left)

    # DFS 시작
    dfs(0, [0] * 11, n)
    return answer