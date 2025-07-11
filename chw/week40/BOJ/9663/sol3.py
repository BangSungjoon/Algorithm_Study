import sys
input = sys.stdin.readline

N = int(input())
count = 0

cols = [False] * N         # 같은 열에 있는지
diag1 = [False] * (2*N)    # ↘ 대각선 (row + col)
diag2 = [False] * (2*N)    # ↙ 대각선 (row - col + N)

def dfs(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N):
        if cols[col] or diag1[row + col] or diag2[row - col + N]:
            continue

        cols[col] = diag1[row + col] = diag2[row - col + N] = True
        dfs(row + 1)
        cols[col] = diag1[row + col] = diag2[row - col + N] = False

dfs(0)
print(count)