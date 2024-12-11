from itertools import product

def solution(n, info):
    info.reverse() # 점수를 0점부터 10점까지 순서로 변경
    ans = [-1]
    max_diff = 0  # 라이언과 어피치 점수 차의 최대값

    # 가능한 모든 승패 조합 순회
    ## True: 라이언이 해당 점수에서 승리
    ## False: 어피치가 승리 또는 비김
    for winlose in product((True, False), repeat=11):
        # 현재 조합에서 필요한 화살의 개수
        arrow = sum(info[i] + 1 for i in range(11) if winlose[i])

        # 필요한 화살이 n을 초과하면 해당 조합은 불가능하므로 스킵
        if arrow <= n:
            # 어피치 점수 : 어피치가 승리한 점수만 더함
            apeach = sum(i for i in range(11) if not winlose[i] and info[i])
            # 라이언 점수 : 라이언이 승리한 점수만 더함
            ryan = sum(i for i in range(11) if winlose[i])

            # 점수 차이
            diff = ryan - apeach

            # 점수 차이가 최대 점수 차보다 크면 결과를 업데이트
            if diff > max_diff:
                max_diff = diff  # 최대 점수 차 갱신
                # 현재 조합에 맞는 화살 배치 배열
                ans = [info[i] + 1 if winlose[i] else 0 for i in range(11)]
                # 남은 화살을 0점에 배치
                ans[0] += n - arrow
                
    ans.reverse()
    return ans
