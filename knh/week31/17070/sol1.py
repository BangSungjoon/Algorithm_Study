# [G5] 17070 파이프 옮기기 1

# STEP 1. 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]   # 0은 공간, 1은 벽

# STEP 2. 순회 시작
stack = [((0, 0), (0, 1))]  # ((시작점), (끝점)) 형태로 stack에 저장, 0 ~ N-1 범위
count = 0                   # (N-1, N=1)로 이동시키는 가지수

while stack:
    start, end = stack.pop()

    # STEP 3. 지금 값이 마지막 값이라면 count 증가
    if end == (N-1, N-1):
        count += 1

    # STEP 4. 가로/세로/대각선 헝태 파악
    else:
        # 가로 조건:
        if start[0] == end[0]:
            # 오른쪽으로 이동하는 경우
            nx, ny= end[0], end[1]+1
            if ny < N and arr[nx][ny] == 0:
                stack.append((end, (nx, ny)))   # stack에 추가
                # 대각선으로 이동하는 경우
                nx += 1
                if nx < N and ny < N and arr[nx][ny] == 0 and arr[nx-1][ny] == 0 and arr[nx][ny-1] == 0:
                    stack.append((end, (nx, ny)))   # stack에 추가
        # 세로 조건:
        elif start[1] == end[1]:
            # 아래쪽으로 이동하는 경우
            nx, ny = end[0] + 1, end[1]
            if nx < N and arr[nx][ny] == 0:
                stack.append((end, (nx, ny)))  # stack에 추가
                # 대각선으로 이동하는 경우
                ny += 1
                if nx < N and ny < N and arr[nx][ny] == 0 and arr[nx-1][ny] == 0 and arr[nx][ny-1] == 0:
                    stack.append((end, (nx, ny)))  # stack에 추가
        # 대각선 조건
        else:
            # 오른쪽으로 이동하는 경우
            nx, ny = end[0], end[1] + 1
            if ny < N and arr[nx][ny] == 0:
                stack.append((end, (nx, ny)))  # stack에 추가
                # 대각선으로 이동하는 경우
                nx += 1
                if nx < N and ny < N and arr[nx][ny] == 0 and arr[nx-1][ny] == 0 and arr[nx][ny-1] == 0:
                    stack.append((end, (nx, ny)))  # stack에 추가

            # 아래쪽으로 이동하는 경우
            nx, ny = end[0] + 1, end[1]
            if nx < N and arr[nx][ny] == 0:
                stack.append((end, (nx, ny)))  # stack에 추가

print(count)