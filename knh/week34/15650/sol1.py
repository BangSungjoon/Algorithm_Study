# [S3] 15650 N과 M(2)

from itertools import combinations

# STEP 1. 입력 받기
N, M = map(int, input().split())

# STEP 2. 길이가 M인 모든 수열 구하기
arr = [i for i in range(1, N+1)]
nCr = combinations(arr, M)

for combi in nCr:
    print(*combi)