# 백준 A -> B
# BFS로 풀어보자
a, b = map(int, input().split())
cnt = 1

q = []
q.append([a, 1]) # 현재 숫자, 횟수

while q:
    n, cnt = q.pop(0)
    if n == b:
        break
    if n > b:
        continue

    q.append([n*2, cnt+1])
    c = int(str(n) + '1')
    q.append([c, cnt+1])

if n == b:
    print(cnt)
else:
    print(-1)