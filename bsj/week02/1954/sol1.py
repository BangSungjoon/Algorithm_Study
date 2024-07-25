T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    dx = [1, 0, -1, 0] # x축 이동 벡터
    dy = [0, 1, 0, -1] # y축 이동 벡터
    snail = [[0 for i in range(N)] for j in range(N)] # 2차원 리스트 생성
    count = 1 # 내부에 들어갈 값
    a, b, j = 0, 0, 0 # 좌표 관련 변수

    while count <= N*N:
        snail[a][b] = count # 해당 좌표에 값 넣기
        if 0 <= a+dy[j] < N and 0 <= b+dx[j] < N: # 좌표가 범위를 넘지 않는다면
            if snail[a+dy[j]][b+dx[j]] == 0: # 이동할 좌표의 내용이 0이라면
                a += dy[j] # 이동!
                b += dx[j]
            else:   # 이동활 좌표의 내용이 0이 아니라면 -> 방향 수정 필요
                if j == 3: # j가 3일 땐, j를 늘리지않고 0으로 회귀
                    j = 0 # -> 방향 수정
                    a += dy[j] # 이동!
                    b += dx[j]
                else:
                    j += 1 # j를 다음 값으로 이동 -> 방향 수정
                    a += dy[j]
                    b += dx[j]
        else: # 좌표가 범위를 넘었다면 -> 방향 수정 필요
            if j == 3:
                j = 0 # 방향 수정
                a += dy[j]
                b += dx[j]
            else:
                j += 1 # 방향 수정
                a += dy[j]
                b += dx[j]
        count += 1 # 들어갈 숫자 1 증가

    print(f'#{test_case}')
    for i in snail:
        for j in i:
            print(j, end=' ')
        print()

