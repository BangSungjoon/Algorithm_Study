# N-Queen
# n*n 체스판에 n개의 퀸을 놔야하니 모든 열에 전부 퀸이 있어야 한다.
# 왼쪽 위에서 오른쪽 아래로 향하는 대각선의 좌표들은 j-i가 같다.
# 오른쪽 위에서 왼쪽 아래로 향하는 대각선의 좌표들은 i+j가 같다.
def dfs(cnt):
    global result, n
    if cnt == n:
        result += 1
        return

    for i in range(n):
        if arr[i] == 0 and leftup_rightdown[cnt-i] == 0 and rightup_leftdown[i+cnt] == 0:
            arr[i] = leftup_rightdown[cnt-i] = rightup_leftdown[i+cnt] = 1
            dfs(cnt+1)
            arr[i] = leftup_rightdown[cnt - i] = rightup_leftdown[i + cnt] = 0

n = int(input())
arr = [0]*n
leftup_rightdown = [0]*(2*n-1)
rightup_leftdown = [0]*(2*n-1)

result = 0
dfs(0)
print(result)