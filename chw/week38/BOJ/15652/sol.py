from itertools import product

N, M = list(map(int, input().split()))
arr = list(range(1, N+1))

perm = list(product(arr, repeat=M))
ans = set()

for p in perm:
    p = list(p)
    p.sort()
    p = tuple(p)
    ans.add(p)

ans_list = list(ans)
ans_list.sort()

for a in ans_list:
    print(*a)