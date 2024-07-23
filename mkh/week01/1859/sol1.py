T = int(input())

for tc in range (1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    balance = 0
    wallet = 0
    for i in range(0,N):
        if price[i]==max(price[i:]):
            wallet += price[i]*balance
            balance = 0
        else:
            wallet -= price[i]
            balance += 1
    print(f'#{tc} {wallet}')