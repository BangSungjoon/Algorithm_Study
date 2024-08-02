import sys
sys.stdin = open('sample_input (3).txt','r')

T=int(input())
for tc in range(1, T + 1):
    N= str(input)
    bell, k= map(str, input().split())
    print(bell, k)
    k=int(k)
    
    if bell =='.o.':
       if k==0:
            res=1
       if k%2==1:
            res=0
       if k%2==0:
            res=1   

    if bell == 'o..':
        if k==0:
            res=0
        if k%2==1:
            res=1
        if k%2==0:
            res=0

    if bell == '..o':
        if k==0:
            res=2
        elif k%2==1:
            res=1
        elif k%2==0:
            res=0

    print(f'#{tc} {res}')



# 오답
# 채점용 input 파일로 채점한 결과 fail 입니다.
# (오답 : 41개의 테스트케이스 중 40개가 맞았습니다.)

#1 0
#2 1
#3 0
