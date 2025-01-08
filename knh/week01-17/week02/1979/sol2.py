# 1979 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1) :
    # N : 퍼즐의 가로, 세로 길이 (5 <= N <= 15)
    # K : 단어의 길이 (2 <= K <= N)
    N , K = map(int, input().split())

    # 퍼즐 2차원 배열 생성
    puzzle = []
    for i in range(N) :
        puzzle.append(list(map(int, input().split())))

    # 정답 변수
    answer = 0

    # 1(흰색 칸)이 연달아 몇개 있는지 체크
    for i in range(N) :
        # 가로 or 세로 검사를 위한 변수
        cnt = 0

        # 가로 확인
        for j in range(N) :
            # 칸이 흰색이면, cnt 증가
            if puzzle[i][j] == 1:
                cnt += 1
            # 칸이 검정색이거나, 마지막 칸이면 cnt와 K가 맞는지 확인
            if puzzle[i][j] == 0 or j == N-1 :
                if cnt == K :
                    answer += 1
                cnt = 0
    

        # 세로 확인
        for j in range(N) :
            # 칸이 흰색이면, cnt 증가
            if puzzle[j][i] == 1 :
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1 :
                if cnt == K :
                    answer += 1
                cnt = 0

    # 정답 출력 (형식 : # 테스트케이스 정답)
    print(f'#{t} {answer}')