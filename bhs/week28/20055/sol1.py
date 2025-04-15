# depue로 화면 레고
# 가장 먼저 올라간 로봇부터 앞으로 이동
# 다음 칸이 내구도 존재, 로봇도 없고, 현재 로봇이 존재하는 경우 진행
# 올리는 위치에 내구도 0이 아니고, 로봇이 처름에 존재하지 않으면 로봇 올리기
# 내구도 0인 칸 수가 k개 이상이면 스탑


from collections import deque

n, k = map(int, input().split())
A = deque(map(int, input().split()))  # 내구도
robot = deque([0] * n)  # 로봇은 위쪽 n칸에만 존재할 수 있음
step = 0

while True:
    step += 1

    # 1. 벨트 + 로봇 같이 회전
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내리는 위치에 도달하면 즉시 내림

    # 2. 로봇 이동 (가장 먼저 올라간 로봇부터)
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and A[i + 1] >= 1:
            robot[i] = 0
            robot[i + 1] = 1
            A[i + 1] -= 1
    robot[-1] = 0  # 도착 위치에 있으면 내림

    # 3. 로봇 올리기
    if A[0] >= 1 and robot[0] == 0:
        robot[0] = 1
        A[0] -= 1

    # 4. 내구도 0인 칸 개수 체크
    if A.count(0) >= k:
        break

print(step)