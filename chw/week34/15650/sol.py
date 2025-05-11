from itertools import combinations

N, M = list(map(int, input().split()))
arr = list(range(1, N+1))
ans = list(combinations(arr, M))
for t in ans:
    print(*t)
