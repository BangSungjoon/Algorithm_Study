# [백준] 구간 합 구하기 4
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]*n
prefix_sum[0] = arr[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

i_j = [list(map(int, input().split())) for _ in range(m)]

for idx in range(m):
    i, j = i_j[idx]
    if i == 1:
        print(prefix_sum[j-1])
    else:
        print(prefix_sum[j-1] - prefix_sum[i-2])