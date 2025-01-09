def solution(n, m, section):
    answer = 1
    current_end = section[0] + m - 1
    
    for s in section[1:]:
        if s > current_end:
            answer += 1
            current_end = s + m - 1
    
    return answer