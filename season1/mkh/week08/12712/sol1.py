T = int(input())
delta1 = ((1,0), (-1,0), (0,1), (0,-1))
delta2 = ((1,1), (1,-1), (-1,1), (-1,-1))

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]
    max_flies = 0
    for y in range(N):
        for x in range(N):
            fly_c= fly_d = flies[y][x]
            # 파리 잡는 시작점을 잡고 초기값 세팅. c는 cross(가로세로), d는 diagonal(대각선)
            for power in range(1, M):
                for dy, dx in delta1:
                    if 0 <= y + dy * power < N and 0 <= x + dx * power < N:
                        fly_c += flies[y + dy * power][x + dx * power]
                for dy, dx in delta2:
                    if 0 <= y + dy * power < N and 0 <= x + dx * power < N:
                        fly_d += flies[y + dy * power][x + dx * power]
            # 가로 세로로 분사하면서 fly들에 더해주기
            if max_flies < max(fly_c, fly_d):
                max_flies = max(fly_c, fly_d)
            # 만약 지금까지 잡은 값이 더 크다면 최대값 갱신

    print(f'#{tc} {max_flies}')
