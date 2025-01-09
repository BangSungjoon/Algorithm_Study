import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(str, input().split())) for _ in range(N)]
#     cnt = 0
#     result = ''
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '#':
#                 for k in range(N):
#                     if arr[i+k][j] == '#':
#                         cnt += 1
#                     else:
#                         break
#                         result = 'yes'
#                 for l in range(cnt):
#                     if arr[i+k][j+l] == '#':
#                         if


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]     # 배열 만들기
    woomooljung, pos_row, pos_col = 0, 0, 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] == '#':
                woomooljung += 1              # #이 있는 곳을 발견한다면 '#'의 개수 세기
                if woomooljung == 1:          # #이 1개 있다면 그 좌표 찍기
                    pos_row = row
                    pos_col = col

    side = 0
    total = 0
    for i in range(pos_col, n):         # #이 있는 좌표에서 가로 방향으로 #을 탐색하기
        if arr[pos_row][i] == '#':      # #이 있으면 side와 total에 추가
            side += 1
            total += 1
        else:
            break                       # 없으면 정사각형 아니므로 break


    check, side_row = False, 1
    for j in range(pos_row + 1, n):     # #이 있는 자리에서 한칸 아래부터 탐색
        cnt = 0
        side_row += 1                   # 아래로 얼마나 갔는지 체크
        if side_row> side:              # #이 있는 side보다 side_row가 크면 break
            break
        for i in range(pos_col, n):
            if arr[j][i] == '#':        # 한칸 아래 이동 후 #이 있는지 확인
                cnt += 1                # #있을 때마다 cnt와 total의 개수 1씩 추가
                total += 1
            else:
                break
        if cnt != side:                 # side(열) cnt(행)이 같아야함 > 둘이 다르면
            check = True                #  check를 1로 줌
            break

    if total == woomooljung and not check:            # 탐색한 #의 개수도 같고,  가로세로 체크도 같으면
        print(f'#{tc} \'yes\'')
    else:
        print(f'#{tc} \'no\'')