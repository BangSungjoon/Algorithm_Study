T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, (input().split()))
    word_map = []

    for i in range(N): # 2차원 배열 입력 받기
        word_map.append(list(map(int, input().split())))

    answer = 0 # 정답
    for i in range(N): # 행 탐색
        check = 0 # 연속된 1의 수
        for j in range(N):
            if word_map[i][j] == 1: # 1이라면 check 하나 추가
                check += 1
            else: # 1이 아니라면 check 초기화
                if check == K: # 다만, check가 K라면 초기화 전 정답 1증가
                    answer += 1
                check = 0
        if check == K: # 연속된 1의 수가 K와 일치한다면 정답 1증가
            answer += 1

    for i in range(N): # 열 탐색
        check = 0
        for j in range(N):
            if word_map[j][i] == 1:
                check += 1
            else:
                if check == K:
                    answer += 1
                check = 0
        if check == K:
            answer += 1

    print(f'#{test_case} {answer}')
