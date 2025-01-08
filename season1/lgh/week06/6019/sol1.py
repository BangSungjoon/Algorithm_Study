import sys
sys.stdin=open('s_input.txt')

T=int(input())
for tc in range(1,T+1):
    D, A, B, F= map(int, input().split())
    time=0
    distance=0
    time= D / (A+B)
    distance=time*F
    print(f'#{tc}', distance)