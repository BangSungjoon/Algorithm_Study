import sys
sys.stdin=open('s_input (1).txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input()) #버스 노선 개수 입력받기
    arr= [list(map(int,input().split()))for _ in range(N)]  #노선 범위를 2차원배열리스트로 입력받기 
    # print(arr)    #[[1, 3], [2, 5]]
    P=int(input()) # 정류장 개수 입력받기
    C=[int(input())for _ in range(P)]  # 정류장 번호 리스트로 입력 받기 #[1, 2, 3, 4, 5]
    res=[0]*P   # 출력할 결과(각 정류장마다 몇 개의 버스 노선이 지나는지 기록할 리스트)
    # print(C)
   
    for i in range(N):  #버스 노선 개수(N) 만큼 순회
        for j in range(P): # j는 각 정류장 , 전체 정류장 개수만큼 순회
            if C[j] in range(arr[i][0], arr[i][1]+1): #해당 정류장이 노선 범위안에 있는지 조건
                res[j]+=1 # 해당 정류장에 다니는 버스 노선의 수 1증가

    print(f'#{tc}', *res)

  

