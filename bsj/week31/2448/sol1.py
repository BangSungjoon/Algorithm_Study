# 백준 2448번 별찍기 - 11
def samgak(h, x, y):
    if h == 3:
        arr[y][x] = '*'
        arr[y+1][x-1] = arr[y+1][x+1] = '*'
        arr[y+2][x-2] = arr[y+2][x-1] = arr[y+2][x] = arr[y+2][x+1] = arr[y+2][x+2] = '*'
    else:
        half = h // 2
        samgak(half, x, y)
        samgak(half, x-half, y+half)
        samgak(half, x+half, y+half)

N = int(input())
arr = [[' ' for _ in range(N*2-1)] for _ in range(N)]
samgak(N, N-1,0)
for row in arr:
    print(''.join(row))