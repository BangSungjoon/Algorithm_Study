# [백준] 문제집
import heapq

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
tree = [[] for _ in range(n+1)]
indegree = [0]*(n+1)    # 진입 차수: 해당 idx의 값은 선행되어야 하는 남은 문제의 수

# 선행 문제 그래프를 그리고, 진입 차수 계산
for x, y in arr:
    tree[x].append(y)
    indegree[y] += 1

q = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)    # 번호가 작은 순으로 자동 정렬됨

result = []
while q:
    current = heapq.heappop(q)  # 현재 가능한 문제 중 가장 작은 번호가 나온다.
    result.append(current)

    for next in tree[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            # 선행 문제가 다 풀렸다면 풀 문제에 추가하기
            heapq.heappush(q, next) # 자동 정렬

print(*result)