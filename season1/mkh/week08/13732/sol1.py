T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    xys = []
    flag = False
    for i in range(N):
        for j in range(N):
            if board[i][j]=='#':
                xys.append((i, j))      
    # #의 좌표들을 xys에 append
    n = int(len(xys)**.5)

    if n == len(xys)**.5:     # 길이의 루트값 == 길이의 루트값의 정수변환형인 경우
        for y in range(n):
            for x in range(n):
                if ((y+xys[0][0]),(x+xys[0][1])) not in xys:        # xys의 0번째 값 즉 제일 왼쪽 위의 값에서 정사각형의 변 길이 만큼 더한 값들이 xys에 없다면
                    flag = True
                    print(f'#{tc} no')                              # no를 프린트하고 나간다.
                    break
            if flag: break
        else: print(f'#{tc} yes')
    else: print(f'#{tc} no')                # #의 개수가 애초에 정사각형을 만들 수 없다면 no를 뱉고 끝낸다.