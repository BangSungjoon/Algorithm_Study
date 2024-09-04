import sys
sys.stdin = open('input.txt', 'r')

# 최대 파리 수 찾는 함수
def max_flies(N, M, arr, type):
    max_catch = 0
    for i in range(N):
        for j in range(N):
            catch = arr[i][j]  # 가운데 값
            for di, dj in type:
                ni, nj = i, j
                for _ in range(M - 1):
                    ni += di
                    nj += dj
                    if 0 <= ni < N and 0 <= nj < N:
                        catch += arr[ni][nj]
            max_catch = max(max_catch, catch)
    return max_catch

# 좌우상하 방향
def max_flies_plus(N, M, arr):
    type = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    return max_flies(N, M, arr, type)

# 대각선 방향
def max_flies_x(N, M, arr):
    type = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    return max_flies(N, M, arr, type)

# 결과 출력
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = max(max_flies_plus(N, M, arr), max_flies_x(N, M, arr))
    print(f'#{tc} {result}')