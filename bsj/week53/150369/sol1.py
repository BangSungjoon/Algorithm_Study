# [프로그래머스] 150369. 택배 배달과 수거하기
def solution(cap, n, deliveries, pickups):
    answer = 0
    need_d = 0
    need_p = 0
    
    for i in range(n-1, -1, -1):
        need_d += deliveries[i]
        need_p += pickups[i]
        
        while need_d > 0 or need_p > 0:
            answer += (i+1)*2
            need_d -= cap
            need_p -= cap
            
    return answer