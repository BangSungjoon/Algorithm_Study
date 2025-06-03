def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    end_point = -1
    
    for s, e in targets:
        if s >= end_point:
            end_point = e
            answer += 1
    return answer