import sys
sys.stdin=open('sample_input (7).txt')


def dfs(row, sum):
    global min   #함수밖에서 선언한 변수를 사용하기 위해 global
    if row==N:
        if min > sum:
            min = sum
            return min
    for col in range(N):
        if visited[col] == 0:
            visited[col]=1
            dfs(row+1, sum + arr[row][col])    
            visited[col] =0

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    visited=[0]*N
    min=101

    dfs(0,0)  #row=0 sum=0으로 호출

    print(f'#{tc} {min}')