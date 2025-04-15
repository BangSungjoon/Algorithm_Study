# [S1] 1932 정수 삼각형

# STEP 1. 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 함수 정의
def DP(x, y):
    if x == N - 1:
        return arr[x][y]
    else:
        return max(DP(x+1, y), DP(x+1, y+1)) + arr[x][y]

# STEP 3. 출력
print(DP(0,0))