# [백준] 바이러스
def dfs(node):
    global cnt
    visited[node] = 1
    cnt += 1
    for i in adj_l[node]:
        if visited[i] == 0:
            dfs(i)

n = int(input())    # 컴퓨터의 수
m = int(input())    # 컴퓨터 쌍의 수
adj_l = [[] for _ in range(n+1)]
cnt = 0

for _ in range(m):
    num1, num2 = map(int, input().split())
    adj_l[num1].append(num2)
    adj_l[num2].append(num1)

visited = [0] * (n+1)
dfs(1)

print(cnt-1)