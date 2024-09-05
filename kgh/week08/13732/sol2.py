import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 1단계 모든 # 좌표 리스트
    positions = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == '#']

    # #의 시작점과 끝점 찾기
    start_i = min(pos[0] for pos in positions)
    end_i = max(pos[0] for pos in positions)
    start_j = min(pos[1] for pos in positions)
    end_j = max(pos[1] for pos in positions)

    # 정사각형의 크기
    side_len = end_i - start_i + 1

    # 정사각형 여부 확인
    is_square = (end_j - start_j + 1 == side_len)  # 가로, 세로 길이 같아야 함
    if is_square:
        for i in range(start_i, start_i + side_len):
            for j in range(start_j, start_j + side_len):
                if arr[i][j] != '#':
                    is_square = False
                    break
            if not is_square:
                break

    result = "yes" if is_square else "no"
    print(f"#{tc} {result}")
