T = int(input())

for tc in range (1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    max_future = []
    wallet = 0
    balance = 0

    for i in range(N):
        max_future.append(0)
    
    max_future[-1] = price[-1]
    
    for i in range(N-1,0,-1):
        if price[i-1]>max_future[i]:
            max_future[i-1]=price[i-1]
        else: max_future[i-1]=max_future[i]

    for i in range(N):
        if price[i]==max_future[i]:
            wallet += price[i]*balance
            balance = 0
        else:
            wallet -= price[i]
            balance += 1

    print(f'#{tc} {wallet}')
