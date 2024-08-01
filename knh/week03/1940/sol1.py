# 1940 가랏! RC카!

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = 0 # 총 이동거리 저장 변수
    speed = 0

    for n in range(N):
        tmp = list(map(int, input().split()))
        
        if len(tmp) == 2 :
            mode, speed_change = tmp
            # 가속
            if mode == 1:
                speed += speed_change
            # 감속
            elif mode == 2 :
                if speed - speed_change > 0 :
                    speed -= speed_change
                else :
                    speed = 0
            
        result += speed
    
    print(f'#{t} {result}')

        