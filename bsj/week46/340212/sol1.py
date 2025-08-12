def solution(diffs, times, limit):
    # 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하려고 한다.
    # -> 이분 탐색? 1부터 limit까지
    answer = 0
    start = 1
    end = limit
    while start <= end:
        mid = (start + end) // 2    # 내 숙련도
        spend_time = 0
        for i in range(len(diffs)):
            if mid >= diffs[i]:
                spend_time += times[i]
            else:
                if i == 0:
                    spend_time += times[i]*(diffs[i]-mid) + times[i]
                else:
                    spend_time += ((times[i]+times[i-1])*(diffs[i]-mid)) + times[i]
            if spend_time > limit:
                break
        if spend_time <= limit:
            # 소요 시간이 시간제한보다 작다면 숙련도를 줄이기
            answer = mid
            end = mid - 1
        else:
            # 소요 시간이 시간제한보다 크다면 숙련도를 늘리기
            start = mid + 1
        
    return answer