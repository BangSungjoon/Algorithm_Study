def find_time(lv, diffs, times, limit):
    time_spent = 0

    for i in range(len(diffs)):
        # STEP 1. 변수 설정
        curr_diff = diffs[i]
        curr_time = times[i]
        prev_time = times[i-1] if i > 0 else 0

        # STEP 2. 소요 시간 계산
        if lv < curr_diff:
            time_spent += (curr_diff - lv) * (curr_time + prev_time) + curr_time
        else:
            time_spent += curr_time

        # STEP 3. 제한 시간 조건 확인
        if time_spent > limit:
            return False
    return True
        
def solution(diffs, times, limit):
    num = len(diffs)
    
    max_lv, min_lv = max(diffs), 1
    
    # STEP 1. 이분 탐색으로 숙련도 최솟값 찾기
    while min_lv < max_lv:  
        curr_lv = (max_lv + min_lv)//2
        
        solved = find_time(curr_lv, diffs, times, limit)
         
        if solved:                  # 풀이 성공시
            max_lv = curr_lv        # 최대값 낮추기
        else:                       # 풀이 실패시
            min_lv = curr_lv + 1    # 최소값 높이기

    return min_lv