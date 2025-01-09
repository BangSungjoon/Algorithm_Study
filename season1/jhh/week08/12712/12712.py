import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    i_flies = [list(map(int, input().split())) for _ in range(N)]

    max_died = 0
    for i in range(N):
        for j in range(N):
            sum_died_f = i_flies[i][j]
            sum_died_t = i_flies[i][j]
            di_f = [0, 1, 0, -1]
            dj_f = [1, 0, -1, 0]
            di_t = [1, 1, -1, -1]
            dj_t = [1, -1, -1, 1]
            k = 1
            while k < M:
                for l in range(4):
                    ni_f, nj_f, ni_t, nj_t = i+(di_f[l])*k, j+(dj_f[l])*k, i+(di_t[l])*k, j+(dj_t[l])*k
                    if 0 <= ni_f <= N-1 and 0 <= nj_f <= N-1:
                        sum_died_f += i_flies[ni_f][nj_f]
                    if 0 <= ni_t <= N-1 and 0 <= nj_t <= N-1:
                        sum_died_t += i_flies[ni_t][nj_t]
                k += 1
            if sum_died_f > sum_died_t and sum_died_f > max_died:
                max_died = sum_died_f
            elif sum_died_t > sum_died_f and sum_died_t > max_died:
                max_died = sum_died_t

    print(f'#{tc} {max_died}')







