# 백준 트리의 부모 찾기
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때,
# 각 노드의 부모를 구하는 프로그램을 작성하시오.
import sys
sys.setrecursionlimit(10**5 + 5)
input = sys.stdin.readline

def dfs(idx):
    # idx: 현재 방문 중인 노드
    if adj_l[idx]:
        for i in adj_l[idx]:
            # print('i는', i)
            if result[i] == 0:  # 방문한 적이 없다면
                result[i] = idx # 현재 방문 중인 노드가 부모임
                dfs(i)

n = int(input())
adj_l = [[] for _ in range(n+1)]
result = [0]*(n+1)
result[1] = 'root'

for _ in range(n-1):
    x, y = map(int, input().split())
    adj_l[x].append(y)
    adj_l[y].append(x)
# print(adj_l)
dfs(1)
# print(result)
for i in range(2, n+1):
    print(result[i])