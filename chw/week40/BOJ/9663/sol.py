import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

# N퀸이 성립 하는지 체크
def check(board):
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                for i in range(1, N):
                    for dx, dy in [(-i, -i), (-i, i), (i, i), (i, -i)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
                            return False
    return True

cnt = 0
for col in permutations(range(N), N):
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        board[i][col[i]] = 1

    ans = check(board)
    if ans:
        cnt += 1

print(cnt)