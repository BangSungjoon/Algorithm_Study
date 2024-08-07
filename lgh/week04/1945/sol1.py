#간단한 소인수분해
import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    dict={2:0, 3:0, 5:0, 7:0, 11:0}
    for key in dict.keys():
        while N % key==0:
              dict[key]+=1
              N=N//key
          

    # print(f'#{tc} {dict.values()}')
    print(f'#{tc}', ' '.join(map(str, dict.values())))   # 딕셔너리값 꺼내올때 출력형식 주의
    