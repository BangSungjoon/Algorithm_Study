import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스의 개수

for tc in range(1, T+1):
    N = int(input())  # Command의 수
    distance = 0  # 총 이동 거리
    velocity = 0  # 현재 속도

    for _ in range(N):
        command = list(map(int, input().split()))
        
        if command[0] == 1:  # 가속
            velocity += command[1]
        elif command[0] == 2:  # 감속
              
            if velocity < command[1]:
                velocity = 0
            '''
            생각 더하기. 현재 속도보다 감속할 속도가 더 클 경우 속도는 0m/s가 된다. 
            if velocity < command[1]:
                velocity = 0
            
            max(0, command[1] - velocity)

            '''


        # 현재 속도로 1초간 이동한 거리를 더함
        distance += velocity

    print(f"#{tc} {distance}")


    # 입력한 값에 시간반영 1->초당2m, 2->초당1m