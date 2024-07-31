T = int(input())

for tc in range(1, T+1):
    N = int(input())
    accu_speed = 0
    dist = 0
    
    for i in range(N):
        command = list(map(int,input().split())) # command를 list로 받아옴.
        if len(command) == 1: # command의 길이가 1일 때, 즉 0일 때 => 현재 속도를 거리에 더해주기
            dist += accu_speed
        else:
            if command[0] ==1: # command가 가속일 경우, 현재 속도에 명령만큼의 가속을 더하고 거리에 누적 속도만큼 더하기
                accu_speed += command[1]
                dist += accu_speed
            else:               # command가 감속일 경우, 현재 속도에 명령만큼의 감속을 빼고 거리에 누적 속도만큼 더하기
                accu_speed -= command[1]
                if accu_speed < 0:
                    accu_speed = 0
                dist += accu_speed

    print(f'#{tc} {dist}')