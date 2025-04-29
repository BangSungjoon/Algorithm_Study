N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]


# 테트로미노 모양
tetrominos = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
        [(0,1), (1,0), (1,1)], # 2x2형태
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]

def hap(i,j,tetromino) :
    temp = arr[i][j] # 시작 위치 기준점
    for di,dj in tetromino :
        # 나머지 위치에 대해서는 범위 내 유효한지 검사
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0<= nj < M :
            temp += arr[ni][nj]
        else :
            return 0
    return temp


ans = 0
for i in range (N) :
    for j in range (M) :
        for tetromino in tetrominos:
            temp = hap(i,j,tetromino) # 현재 위치에서 가능한 모든 모양의 합 계산
            ans = max(temp, ans)

print(ans)