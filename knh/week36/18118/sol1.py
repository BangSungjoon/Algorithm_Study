# [PGM] 18118 요격 시스템

def solution(targets):
    answer = 0
    targets = sorted(targets)
    end = 0
    
    for s, e in targets:
        if s < end:
            end = min(e, end)
        else:
            end = e
            answer += 1
    
    return answer
