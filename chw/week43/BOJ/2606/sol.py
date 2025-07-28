import sys
input = sys.stdin.readline

N = int(input())
T = int(input())

computer = [[] for _ in range(N+1)]

for _ in range(T):
    c1, c2 = map(int, input().split())

    computer[c1].append(c2)
    computer[c2].append(c1)

# 감염된 컴퓨터 정보
infected = [0] * (N+1)
infected[1] = 1

visited = [0] * (N+1)
visited[1] = 1

stack = [*computer[1]]

while stack:
    next_c = stack.pop()

    infected[next_c] = 1

    if visited[next_c] == 0:
        stack.extend(computer[next_c])
        visited[next_c] = 1

print(infected.count(1)-1)