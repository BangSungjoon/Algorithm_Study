n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

max_len = max(map(max, arr))
print(max_len ** 2)