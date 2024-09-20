def solution(n, m, section):
    dists = [section[i+1]-section[i] for i in range(len(section)-1)]
    answer = 1
    temp = 0
    while dists:
        if temp + dists[-1] > m-1:
            answer += 1
            temp = dists.pop()
        else:
            temp += dists.pop()

    return answer



print(solution(8, 4, [2,3,6]))