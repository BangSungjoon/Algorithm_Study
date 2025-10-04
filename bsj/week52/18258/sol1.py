# [백준] 큐 2
from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

q = deque()

for i in range(n):
    order = arr[i]
    if order == 'pop':
        if q:
            num = q.popleft()
            print(num)
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        o, x = order.split()
        q.append(int(x))