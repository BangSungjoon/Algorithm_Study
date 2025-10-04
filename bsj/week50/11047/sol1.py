# [백준] 동전 0
n, k = map(int, input().split())    # n: 동전의 종류, k: 목표하는 금액

wallet = [int(input()) for _ in range(n)]
wallet.sort(reverse=True)
cnt = 0

for money in wallet:
    if money <= k:
        cnt += k // money
        k %= money

        if k == 0:
            break

print(cnt)