# 보급로
# 최소 복구 시간 구하기 

import sys 
sys.stdin=open('input.txt')

def bfs(si, sj, ei, ej): 
    queue = [] 
    inf = 10000 
    visited = [[inf] * N for _ in range(N)] # 최솟값으로 더한 값을 넣을 배열(복구시간을 기록)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1] 
    queue.append((0, 0)) # 0,0 시작점 담기
    ci, cj = 0, 0   # ci, cj는 현재 좌표
    visited[0][0] = 0 # 0,0부터 시작 ( 출발지는 0)
    
    
    
    while queue: # 큐가 빌 동안 반복
        ci, cj = queue.pop(0)  # 현재 좌표 꺼내오기
        for idx in range(4): # 현재좌표 기준으로 상하좌우 델타 탐색
            ni = ci + di[idx]  
            nj = cj + dj[idx]
            if 0 <= ni < N and 0 <= nj < N :  #범위 내에 있으면
                    time = arr[ni][nj] + visited[ci][cj]  # 복구시간 계산(주변 좌표값과 현재좌표의 복구시간 더함)
                    if time < visited[ni][nj]:  # 최소 복구시간을 구함
                        visited[ni][nj] = time 
                        queue.append((ni, nj))  # ni, nj가 다음 순회 시, 기준점(현재좌표)이 됨    
                    
    return visited[ei][ej] # 맨마지막 값(좌표 우하단값)



    
    # while queue: # 큐가 빌 동안 반복
    #     ci, cj = queue.pop(0)  # 현재 좌표 꺼내오기
    #     for idx in range(4): # 델타 탐색
    #         ni = ci + di[idx]  
    #         nj = cj + dj[idx]
    #         if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > arr[ni][nj] + visited[ci][cj]: # 배열 내에 있고, ?
    #             visited[ni][nj] = arr[ni][nj] + visited[ci][cj] 
    #             queue.append((ni, nj))  # ni, nj가 다음 순회 시, 기준점(현재좌표)이 됨              
    # return visited[ei][ej] # 맨마지막 값(좌표 우하단값)
    

T =  int(input())
for tc in range(1, T+1):
    N = int(input())  # N은 지도크기
    arr = [list(map(int, input())) for _ in range(N)]
    
    ans = bfs(0, 0, N-1, N-1)
    print(f'#{tc} {ans}')
    

    
