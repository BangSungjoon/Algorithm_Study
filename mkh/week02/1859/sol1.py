T = int(input())

for tc in range (1,T+1):
    days = int(input())
    future = list(map(int,input().split()))
    balance = 0
    wallet = 0
    for i in range(0,days):
        if future[i]==max(future[i:]):
            wallet += future[i]*balance
            balance = 0
        else:
            wallet -= future[i]
            balance += 1
    print(f'#{tc} {wallet}')