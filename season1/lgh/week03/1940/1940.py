import sys
sys.stdin=open('input (7).txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input()) #커맨드 수
    v=0 #속도
    d=0 #거리

    for i in range(N):
        arr= list(map(int, input().split()))
        if arr[0]== 1:  #가속일 경우
             v += arr[1]  
        elif arr[0]==2:  #감속일 경우 (단, 감속속도더 크면 현재속도 0됨)
            v -= arr[1]
            if v<0: 
                v=0
        d += v #이동거리 계산       
    print(f'#{tc} {d}')                 

