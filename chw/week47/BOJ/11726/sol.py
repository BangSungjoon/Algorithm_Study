from itertools import combinations

n = int(input())

ans = 0

cnt_one = 0
cnt_two = n // 2

# 짝수일 때
if n % 2 == 0:
    cnt_one = cnt_two
    for i in range(cnt_two):
        ans += len(list(combinations(range(cnt_one + i), cnt_two - i)))

# 홀수일 때
else:
    cnt_one = cnt_two + 1
    for i in range(cnt_two):
        ans += len(list(combinations(range(cnt_one+i), cnt_two-i)))

print((ans+1) % 10007)