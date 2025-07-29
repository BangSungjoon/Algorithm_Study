def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)):
            num = progresses.pop(0)
            if num >= 100:
                cnt += 1
                speeds.pop(0)
            else:
                progresses = [num] + progresses[:]
                break

        if cnt:
            answer.append(cnt)
    return answer