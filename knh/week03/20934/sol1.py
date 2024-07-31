# 20934 방울 마술

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1) :
    cup, N = input().split()

    N = int(N)
    
    answer = 0

    if cup == 'o..' : # 방울이 왼쪽에 들어있다면
        if N % 2 == 0 :
            answer = 0 # 왼쪽
        else :
            answer = 1 # 가운데
    elif cup == '.o.' : # 방울이 가운데에 들어있다면
        if N % 2 == 0 :
            answer =   1 # 가운데
        else :
            answer = 0 # 왼쪽
    else : # 방울이 오른쪽에 들어있다면
        if N == 0 : # 움직이지 않았다면
            answer = 2 # 오른쪽
        elif N % 2 == 0:
            answer = 0 # 왼쪽
        else :
            answer = 1 # 가운데
    
    # 출력
    print(f'#{t} {answer}')