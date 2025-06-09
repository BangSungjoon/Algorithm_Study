from itertools import permutations

N, M = map(int, input().split())
seq = list(map(int, input().split()))

perm = permutations(seq, M)
perm = sorted(set(perm))    # 중복 제거

for p in perm:
    print(*p)