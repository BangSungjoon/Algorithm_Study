def solution(n, info):
    max_diff = 0
    best_result = [-1]

    def calculate_score(ryan):
        apeach_score, ryan_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan[i] == 0:
                continue
            if info[i] >= ryan[i]:
                apeach_score += 10 - i
            else:
                ryan_score += 10 - i
        return ryan_score - apeach_score if ryan_score > apeach_score else 0

    def backtrack(idx, arrows_left, ryan):
        nonlocal max_diff, best_result

        # 최대한으로 다 쐈다면
        if idx == 11 or arrows_left == 0:
            ryan[10] += arrows_left
            diff = calculate_score(ryan)
            if diff > max_diff or (diff == max_diff and ryan[::-1] > best_result[::-1]):
                max_diff = diff
                best_result = ryan[:]
            ryan[10] -= arrows_left
            return

        # 어피치가 쏜 화살보다 더 많이 쏠 수 있다면 1. 쏜다
        if arrows_left > info[idx]:
            ryan[idx] = info[idx] + 1
            backtrack(idx + 1, arrows_left - ryan[idx], ryan)
            ryan[idx] = 0

        # 2. 안쏜다
        backtrack(idx + 1, arrows_left, ryan)

    backtrack(0, n, [0] * 11)

    return best_result if max_diff > 0 else [-1]
