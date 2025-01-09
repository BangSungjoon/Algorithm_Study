import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 예시 : [[1, 1], [0], [1, 1]]
 
    distance, speed = 0, 0
 
    for command in arr:
        # 현재 속도 유지
        if command[0] == 0:  # 현재 속도 값 추출
            distance += speed  # 현재 속도로 거리 계산
        # 가속이면
        elif command[0] == 1:
            accel = command[1]  # 가속 값 추출
            speed += accel  # 가속 속도 업데이트
            distance += speed  # 가속 후 거리의 계산
        # 감속이면
        elif command[0] == 2:
            decel = command[1]  # 감속 값 추출
            speed -= decel  # 감소 속도 업데이트
            if speed < 0:  # 속도의 하한값 처리
                speed = 0
            distance += speed  # 감속 후 거리의 계산
 
    print(f"#{tc} {distance}")