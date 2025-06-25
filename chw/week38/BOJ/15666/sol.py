from itertools import combinations_with_replacement

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = []

for combo in combinations_with_replacement(arr, M):
    combo = list(combo)
    combo.sort()

    if combo in ans:
        continue
    else:
        ans.append(combo)

for a in sorted(ans):
    print(*a)