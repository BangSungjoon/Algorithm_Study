# 어짜피 미사일은 요격해야하므로 최대한 뒤에 날라오는 미사일과 겹치게 요격하면 최소가 된다

def solution(targets):
    targets.sort(key=lambda x: x[1])

    missile = targets[0][1] - 0.1
    cnt = 1

    for t in targets:
        if t[0] > missile:
            missile = t[1] - 0.1
            cnt += 1

    return cnt