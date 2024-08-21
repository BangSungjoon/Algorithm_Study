for tc in range(1, 11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]  # 테이블의 형태를 받을 변수 생성.
    cnt = 0                                                     # 교착 상태를 셀 변수 선언.
    for i in range(N):
        stack = [0] * N             # 줄마다 체크할 자성체들을 담을 스택 선언. 최대 길이는 N
        top = -1                    # 스택을 참조할 top -1 선언.
        for j in range(N):
            if table[j][i] == 2 and stack[top] ==1:     # N극에 이끌리는 자성체인데 스택에 마지막에 쌓인 블럭이 S극에 이끌리는 자성체라면
                cnt += 1                                # 교착 상태를 1 더한다
            if table[j][i] != 0:                        # 자성체라면 top에 1을 더하고 스택을 쌓는다.
                top += 1
                stack[top] = table[j][i]
    print(f'#{tc} {cnt}')
