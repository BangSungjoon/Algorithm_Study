def solution(n, computers):
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                computers[j][i] = 1
                computers[i][j] = 1


    cnt = 0
    for i in range(n):
        for j in range(0, i):
            if computers[i][j] == 1:
                cnt += 1



    answer = n - cnt
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(1, [[1]]))