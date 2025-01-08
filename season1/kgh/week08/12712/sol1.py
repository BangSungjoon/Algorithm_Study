import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_catch = 0
    # 상하좌우 방향 스프레이
    for i in range(N):
        for j in range(N):
            catch = arr[i][j]  # 가운데 값
            # 상하좌우 벡터 탐색
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ni, nj = i, j
                # M-1 길이만큼 탐색해야해
                for k in range(M-1):
                    ni += di
                    nj += dj
                    # 배열 안에 속하는 것만 인덱스 제어
                    if 0 <= ni < N and 0 <= nj < N:
                        catch += arr[ni][nj]
            # 최댓값 갱신
            if max_catch < catch:
                max_catch = catch

    # 대각선 방향 스프레이
    for i in range(N):
        for j in range(N):
            catch = arr[i][j]  # 가운데 값
            # 대각선방향 벡터 탐색
            for di, dj in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                ni, nj = i, j
                # M-1 길이만큼 탐색해야해
                for k in range(M-1):
                    ni += di
                    nj += dj
                    # 배열 안에 속하는 것만 인덱스 제어
                    if 0 <= ni < N and 0 <= nj < N:
                        catch += arr[ni][nj]
            # 최댓값 갱신
            if max_catch < catch:
                max_catch = catch

    print(f'#{tc} {max_catch}')