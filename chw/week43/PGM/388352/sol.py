from itertools import combinations

def solution(n, q, ans):
    answer = 0

    num_list = list(range(1, n + 1))
    possible_code = list(combinations(num_list, 5))  # 가능한 5자리 조합

    for code in possible_code:
        for i in range(len(q)):
            t = set(q[i]) & set(code)

            if ans[i] != len(t):
                break
        else:
            answer += 1

    return answer