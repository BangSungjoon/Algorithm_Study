from heapq import heappush, heappop

def solution(jobs):
    time = 0
    q = []
    done = []
    result = 0

    while len(done) != len(jobs):
        for i in range(len(jobs)):
            temp = [i, jobs[i][0], jobs[i][1]]
            if jobs[i][0] <= time and i not in done and temp not in q:
                q.append(temp)

        if not q:
            time += 1
            continue
        else:
            q.sort(key=lambda x: (-x[2], -x[1], -x[0]))
            idx, request, work = q.pop()
            time += work
            done.append(idx)
            result += time - request

    answer = result // len(jobs)
    return answer

jobs = [[0, 3], [1, 9], [3, 5]]
ans = solution(jobs)
print(ans)