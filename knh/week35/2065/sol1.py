# [G5] 2096 내려가기

from sys import stdin

# STEP 1. 입력 받기
N = int(input())
arr = list(map(int, stdin.readline().split())) # 한 줄만 읽기
maxDP = arr
minDP = arr

# STEP 2. 돌면서 max, min 값 계산
for i in range(N-1):
    arr = list(map(int, stdin.readline().split()))    # 한 줄씩 다시 읽기
    maxDP = [arr[0]+max(maxDP[0],maxDP[1]), arr[1]+max(maxDP), arr[2]+max(maxDP[1], maxDP[2])]
    minDP = [arr[0]+min(minDP[0],minDP[1]), arr[1]+min(minDP), arr[2]+min(minDP[1], minDP[2])]

# STEP 3. 출력
print(max(maxDP), min(minDP))

