# Per씨 코드

def solution(n, info):
    answer = []
    max_diff = 0

    def dfs(idx, arrows, lion_info):
        nonlocal answer, max_diff

        if idx == 11:
            if arrows:  # 남은 화살은 모두 0점에 쏘기
                lion_info[10] = arrows

            lion_score = 0
            peach_score = 0
            for i in range(11):
                if lion_info[i] > info[i]:
                    lion_score += 10 - i
                elif info[i] > 0:
                    peach_score += 10 - i

            diff = lion_score - peach_score

            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = [lion_info[:]]
                elif diff == max_diff:
                    answer.append(lion_info[:])
            return

        if arrows > info[idx]:
            next_info = lion_info[:]
            next_info[idx] = info[idx] + 1
            dfs(idx + 1, arrows - next_info[idx], next_info)

        dfs(idx + 1, arrows, lion_info)

    dfs(0, n, [0] * 11)

    if not answer:
        return [-1]

    # 가장 낮은 점수를 더 많이 맞힌 경우 선택
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))