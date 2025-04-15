# [S1] 1932 정수 삼각형

# STEP 1. 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 반복문 사용, 아래에서 위로 올라오며 누적합 계산
for i in range(N-2, -1, -1):
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])

# STEP 3. 출력
print(arr[0][0])