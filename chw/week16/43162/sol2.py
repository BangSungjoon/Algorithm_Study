from collections import deque

def solution(n, computers):
    nodes = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                if j not in nodes[i]:
                    nodes[i].append(j)

    




    return

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))