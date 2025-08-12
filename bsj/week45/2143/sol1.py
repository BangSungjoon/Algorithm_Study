# [백준] 두 배열의 합
t = int(input())
n = int(input())
list_a = list(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))
result = 0

# 모든 누적합이 나오는 경우의 수를 계산
prefix_sum_a = []
prefix_sum_b = []
for i in range(n):
    current = list_a[i]
    prefix_sum_a.append(current)
    for j in range(i+1, n):
        current += list_a[j]
        prefix_sum_a.append(current)

for i in range(m):
    current = list_b[i]
    prefix_sum_b.append(current)
    for j in range(i+1, m):
        current += list_b[j]
        prefix_sum_b.append(current)

prefix_sum_a.sort()
prefix_sum_b.sort(reverse=True)

# 투포인터로 풀기 (idx_a, idx_b)
idx_a, idx_b = 0, 0
while idx_a < len(prefix_sum_a) and idx_b < len(prefix_sum_b):
    total = prefix_sum_a[idx_a] + prefix_sum_b[idx_b]
    if total == t:
        # a와 같은 값이 몇개 인지 봐야함
        cnt_a = 0
        current_a = prefix_sum_a[idx_a]
        while idx_a < len(prefix_sum_a) and prefix_sum_a[idx_a] == current_a:
            idx_a += 1
            cnt_a += 1
        # b와 같은 값도 몇개인지 체크하기
        cnt_b = 0
        current_b = prefix_sum_b[idx_b]
        while idx_b < len(prefix_sum_b) and prefix_sum_b[idx_b] == current_b:
            idx_b += 1
            cnt_b += 1
        result += cnt_a * cnt_b
    elif total > t:
        # 합이 t보다 크다면 값을 줄여야 한다.
        idx_b += 1
    else:
        # 합이 t보다 작다면 값을 늘려야 한다.
        idx_a += 1

print(result)