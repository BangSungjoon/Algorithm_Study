# [G5] 20055 컨베이이어 벨트 위 로봇

from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False] * (2 * N)  # 로봇이 있는 위치 저장

up = 0                    # 로봇이 올라가는 위치
down = N - 1              # 로봇이 내려가는 위치
step = 0                  # 단계 수

while True:
    step += 1

    # 1. 벨트와 로봇이 함께 회전 (배열 회전 대신 인덱스 조작)
    up = (up - 1) % (2 * N)
    down = (down - 1) % (2 * N)
    robot[down] = False  # 내리는 위치에 로봇이 있으면 내림

    # 2. 로봇 이동 (내리는 위치 쪽에서부터)
    for i in range(N - 2, -1, -1):  # 내리는 위치 직전까지
        cur = (up + i) % (2 * N)
        next_pos = (cur + 1) % (2 * N)

        if robot[cur] and not robot[next_pos] and belt[next_pos] > 0:
            robot[cur] = False
            robot[next_pos] = True
            belt[next_pos] -= 1

    robot[down] = False  # 혹시 이동한 로봇이 내려가야 하는 위치에 왔다면 제거

    # 3. 로봇 올리기
    if not robot[up] and belt[up] > 0:
        robot[up] = True
        belt[up] -= 1

    # 4. 내구도 0인 칸 수 체크
    if belt.count(0) >= K:
        print(step)
        break
