# [백준] 트리와 쿼리
import sys
sys.setrecursionlimit(10**6)

def dfs(current, parent):
    dp[current] = 1
    for ad in adj_l[current]:
        if ad != parent: # 부모로 역행을 방지하기
            dfs(ad, current) # 자식 서브쿼리에 속한 정점의 수 더하기
            dp[current] += dp[ad]

# 정점의 수 n, 루트의 번호 r, 쿼리의 수 q
n, r, q = map(int, sys.stdin.readline().split())

# 인접 리스트
adj_l = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    adj_l[u].append(v)
    adj_l[v].append(u)

dp = [0] * (n+1)
dfs(r, -1)

for _ in range(q):
    num = int(sys.stdin.readline())
    print(dp[num])