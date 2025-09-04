def rotate90(arr):
    m = len(arr)
    rot = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rot[i][j] = arr[m-1-j][i]
    return rot

def check_open(k, board, pad, n, m, x, y):
    # 자물쇠의 원래 영역만 검사
    for i in range(n):
        for j in range(n):
            lock_val = board[pad + i][pad + j]
            # pad+i, pad+j: 확장 보드에서 자물쇠 칸의 절대 좌표
            # x, y: 키의 좌상단이 올라간 절대 좌표
            ii = (pad + i) - x
            jj = (pad + j) - y
            key_val = 0
            if 0 <= ii < m and 0 <= jj < m:
                key_val = k[ii][jj]
            # 모든 칸의 합이 정확히 1
            if lock_val + key_val != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    # 회전 시킨 열쇠 배열 만들기
    key90 = rotate90(key)
    key180 = rotate90(key90)
    key270 = rotate90(key180)
    
    # 자물쇠 padding 버전 만들기
    n = len(lock)
    m = len(key)
    pad_size = m - 1
    padding_lock = [[0]*(n + 2*pad_size) for _ in range(n + 2*pad_size)]
    for i in range(n):
        for j in range(n):
            padding_lock[pad_size + i][pad_size + j] = lock[i][j]

    for k in [key,
               key90,
               key180,
               key270]:
        for i in range(0, n + 2*pad_size - m + 1):
            for j in range(0, n + 2*pad_size - m + 1):
                if check_open(k, padding_lock, pad_size, n, m, j, i):
                    answer = True
                    break
            
    return answer