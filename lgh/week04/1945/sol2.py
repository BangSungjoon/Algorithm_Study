import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    lst=[2, 3, 5, 7, 11]
    count=[0, 0, 0, 0, 0]
    for i in range(len(lst)):
        while N % lst[i]==0:
              count[i]+=1
              N=N//lst[i]
          
    print(f'#{tc}', *count)   #출력 주의  , 빼먹지 말기  