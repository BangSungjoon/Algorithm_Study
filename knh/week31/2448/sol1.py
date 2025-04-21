# [G4] 2448 별 찍기 - 11

# STEP 1. 입력 받기
N = int(input())

# STEP 2. 초기 배열 만들기
# 가운데 정렬 하기 위해 2*N-1
arr = [[' ' for _ in range(2 * N - 1)] for _ in range(N)]

# STEP 3. 삼각형 그리기
def draw_star(x, y, size):
    # 작은 삼각형 그리기
    #   *
    #  * *
    # *****
    if size == 3:
        arr[x][y] = '*'
        arr[x + 1][y - 1] = arr[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            arr[x + 2][y + i] = '*'
    # 재귀로 더 큰 삼각형 그리기
    else:
        half = size // 2
        draw_star(x, y, half)                   # 위쪽 삼각형
        draw_star(x + half, y - half, half)     # 왼쪽 아래 삼각형
        draw_star(x + half, y + half, half)     # 오른쪽 아래 삼각형

# STEP 4. 삼각형 전체 그리기
draw_star(0, N - 1, N)

# STEP 5. 출력
for line in arr:
    print(''.join(line))
