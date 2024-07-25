# 1954 달팽이 숫자
# x, y 시작 인덱스만 바꾼 것

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스
T = int(input())

for t in range(1, T+1) :
    # 달팽이의 크기
    N = int(input())

    # 2차원 배열 생성
    snail = [[None for i in range(N)] for j in range(N)]
    
    # 이동 방향
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 방향 전환시 사용하기 위한 이동 방향 index
    move_index = 0

    # 달팽이에 넣을 숫자
    num = 1

    # 순회 시작할 위치의 index 값
    x, y = 0, 0

    while num <= N**2 :
        snail[x][y] = num
        
        # 지금 방향 그대로 갔을 때 다음 달팽이 칸
        tmp_x = x + move[move_index][0]
        tmp_y = y + move[move_index][1]

        # 2차원 배열 크기를 넘었을 경우 or 다음 달팽이 칸이 이미 차있을 경우
        if (tmp_x >= N or tmp_x < 0 or tmp_y >= N or tmp_y < 0) :
            # 다음 방향으로 전환
            # 인덱스 값이니 나머지 연산 필수
            move_index = (move_index + 1) % 4
        elif (snail[tmp_x][tmp_y] != None) :
            move_index = (move_index + 1) % 4
    
        # tmp_x, tmp_y 값 갱신
        x = x + move[move_index][0]
        y = y + move[move_index][1]

        num += 1

    # 정답 출력
    # 테스트 케이스 번호 출력
    print(f'#{t}')
    for i in snail :
        for j in i :
            print(j, end=" ")
        print()