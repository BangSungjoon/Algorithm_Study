T= int(input())
for tc in range(1, T+1):
    N = int(input())
    bat = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0
    for i in range(N//2):
        ans += sum(bat[i][N//2-i:N//2+1+i]) + sum(bat[N-1-i][N//2-i:N//2+1+i])
    ans += sum(bat[N//2])
    print(f'#{tc} {ans}')