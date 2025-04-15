import sys
from  collections import deque

# sys.stdin = open("input.txt")

n, k = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(100001)]

def bfs():
    queue = deque([(n, 0)])
    visited[n] = 1

    while queue:
        current, time = queue.popleft()

        if current == k:
            print(time)
            break

        jump = current*2
        back = current-1
        front = current+1

        if 0 <= jump <= 100000 and visited[jump] == 0:
            queue.append((jump, time))
            visited[jump] = 1

        if 0 <= back <= 100000 and visited[back] == 0:
            queue.append((back, time+1))
            visited[back] = 1
        
        if 0 <= front <= 100000 and visited[front] == 0:
            queue.append((front, time+1))
            visited[front] = 1
            
bfs()