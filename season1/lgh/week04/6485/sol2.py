import sys
sys.stdin=open('s_input (1).txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input()) #버스 노선 개수 입력받기
    arr= [list(map(int,input().split()))for _ in range(N)]  #각 노선의 정류장 범위를 입력받아 2차원리스트arr저장
    # print(arr)    #[[1, 3], [2, 5]]
    P=int(input()) # 확인하고 싶은 정류장 개수를 입력받기
    C=[int(input())for _ in range(P)]  # 각 확인하고 싶은 정류장 번호를 입력 받기 #[1, 2, 3, 4, 5]
    res=[]   # 각 정류장마다 몇 개의 버스 노선이 지나는지 기록할 빈 리스트
    # print(C)
    
   
    for j in C:  # 각 확인하고 싶은 정류장 번호 j에 대해 반복
        cnt=0  # 버스정류장j 에 다니는 노선 수 기록할 변수
        for k in arr: # 각 버스 노선의 범위 k에 대해 반복
            if k[0] <= j <= k[1]: # 정류장 번호 j가 노선 k의 범위 안에 있는지 확인   #첫 번째 반복에서 k는 [1, 3], 두 번째 반복에서 k는 [2, 5]             
                cnt+=1
        res += [cnt]   #cnt 값을 리스트 형태로 변환하여 res에 추가
            
           
 
    print(f'#{tc}', *res)



