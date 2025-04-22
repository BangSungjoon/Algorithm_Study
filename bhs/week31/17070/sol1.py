# dp 드러워서 못 풀겠다.
# dfs로 가로일 경우 가로 세로, 세로일 경우 가로 세로, 대각선일 경우 가로 세로 대각선 이동


def dfs():
    n = int(input())
    house = []
    for _ in range(n):
        house.append(list(map(int, input().split())))
    
    # 파이프의 방향: 0=가로, 1=세로, 2=대각선
    count = [0]  # 결과를 저장할 변수 (리스트로 만들어 참조로 전달)
    
    # r1, c1은 파이프 앞쪽 r2,c2는 파이프프 뒷쪽
    def move_pipe(r1, c1, r2, c2, direction):
        # 파이프의 끝이 목적지(n-1,n-1)에 도달한 경우
        if r2 == n-1 and c2 == n-1:
            count[0] += 1
            return
        
        # 가로 방향인 경우 (오른쪽으로 이동, 오른쪽 아래로 이동)
        if direction == 0:
            # 오른쪽으로 이동
            if c2 + 1 < n and house[r2][c2+1] == 0:
                move_pipe(r2, c2, r2, c2+1, 0)
            
            # 오른쪽 아래 대각선으로 이동
            if r2 + 1 < n and c2 + 1 < n and house[r2][c2+1] == 0 and house[r2+1][c2] == 0 and house[r2+1][c2+1] == 0:
                move_pipe(r2, c2, r2+1, c2+1, 2)
        
        # 세로 방향인 경우 (아래로 이동, 오른쪽 아래로 이동)
        elif direction == 1:
            # 아래로 이동
            if r2 + 1 < n and house[r2+1][c2] == 0:
                move_pipe(r2, c2, r2+1, c2, 1)
            
            # 오른쪽 아래 대각선으로 이동
            if r2 + 1 < n and c2 + 1 < n and house[r2][c2+1] == 0 and house[r2+1][c2] == 0 and house[r2+1][c2+1] == 0:
                move_pipe(r2, c2, r2+1, c2+1, 2)
        
        # 대각선 방향인 경우 (오른쪽으로 이동, 아래로 이동, 오른쪽 아래로 이동)
        elif direction == 2:
            # 오른쪽으로 이동
            if c2 + 1 < n and house[r2][c2+1] == 0:
                move_pipe(r2, c2, r2, c2+1, 0)
            
            # 아래로 이동
            if r2 + 1 < n and house[r2+1][c2] == 0:
                move_pipe(r2, c2, r2+1, c2, 1)
            
            # 오른쪽 아래 대각선으로 이동
            if r2 + 1 < n and c2 + 1 < n and house[r2][c2+1] == 0 and house[r2+1][c2] == 0 and house[r2+1][c2+1] == 0:
                move_pipe(r2, c2, r2+1, c2+1, 2)
    
    # 파이프 초기 위치 (0,0)-(0,1), 방향은 가로(0)
    if house[n-1][n-1] != 1:  # 목적지가 벽이 아닌 경우만 시작
        move_pipe(0, 0, 0, 1, 0)
    
    return count[0]

print(dfs())