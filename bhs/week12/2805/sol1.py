T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    get_farm = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i, N//2+1+i):
                get_farm += farm[i][j]
            else:
                for j in range(i-N//2, N+N//2-i):
                    get_farm += farm[i][j]
print(f'#{tc} {get_farm}')
