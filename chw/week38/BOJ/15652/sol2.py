from itertools import combinations_with_replacement

N, M = list(map(int, input().split()))
arr = list(range(1, N+1))

for a in combinations_with_replacement(arr, M):
    print(*a)