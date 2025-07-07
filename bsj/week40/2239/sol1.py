def solve(idx):
    """
    스도쿠 판의 빈 칸(zeros 리스트)의 idx번째 칸을 채우는 함수

    :param idx: 현재 zeros 리스트에서 몇 번째 빈 칸을 채울 차례인지 나타내는 인덱스 값
    """
    if idx == len(zeros):
        # 모든 빈 칸을 다 채웠다면 완성된 스도쿠 판을 출력
        for row in board:
            print("".join(map(str, row)))
        exit()  # 정답 한 개만 출력하고 종료

    y, x = zeros[idx]   # 현재 채울 빈 칸의 좌표(y, x)
    for num in range(1, 10):
        if check(y, x, num):
            board[y][x] = num   # num을 해당 칸에 넣고
            solve(idx + 1)      # 다음 빈 칸으로 이동(재귀 호출)
            board[y][x] = 0     # 백트래킹

def check(y, x, num):
    """
    현재 (y, x) 위치에 num을 넣을 수 있는지 확인하는 함수

    :param y: 빈 칸의 행 인덱스
    :param x: 빈 칸의 열 인덱스
    :param num: 넣으려는 숫자(1~9)
    :return: num을 넣어도 규칙에 맞다면 True, 맞지 않다면 False
    """

    # 가로
    for i in range(9):
        if board[y][i] == num:
            return False
    # 세로
    for i in range(9):
        if board[i][x] == num:
            return False
    # 3x3
    sy, sx = y//3*3, x//3*3
    for i in range(sy, sy+3):
        for j in range(sx, sx+3):
            if board[i][j] == num:
                return False
    return True

board = [list(map(int, input().strip())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
solve(0)
