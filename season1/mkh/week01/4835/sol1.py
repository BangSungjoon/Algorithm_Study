T = int(input())
for tc in range(1,T+1):
    N, M= map(int,input().split())
    numbers = list(map(int,input().split()))
    ls=[]
    for i in range(0,N-M+1):
        num_sum = 0
        for j in range(0,M):
            num_sum+=numbers[i+j]
        ls.append(num_sum)
    print(f'#{tc} {max(ls)-min(ls)}')