# [백준] 꿀 따기
n = int(input())
arr = list(map(int, input().split()))
total = 0

# 벌통이 오른쪽 끝일 경우
prefix_sum = [0]*n
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for i in range(1, n-1):
    # i는 bee2의 위치
    bee1 = prefix_sum[-1] - arr[i]
    bee2 = prefix_sum[-1] - prefix_sum[i]

    if total < bee1 + bee2:
        total = bee1 + bee2

# 벌통이 왼쪽 끝일 경우
prefix_sum2 = [0]*n
for i in range(n-2, -1, -1):
    prefix_sum2[i] = prefix_sum2[i+1] + arr[i]

for i in range(n-2, 0, -1):
    # i는 bee2의 위치
    bee1 = prefix_sum2[0] - arr[i]
    bee2 = prefix_sum2[0] - prefix_sum2[i]

    if total < bee1 + bee2:
        total = bee1 + bee2

# 벌통이 가운데 있을 경우
for i in range(1, n-1):
    # i는 벌통의 위치
    bee1 = prefix_sum[i]
    bee2 = prefix_sum2[i]

    if total < bee1 + bee2:
        total = bee1 + bee2

print(total)