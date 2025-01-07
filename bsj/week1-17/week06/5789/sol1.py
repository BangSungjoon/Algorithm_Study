# 5789. 현주의 상자 바꾸기
T = int(input())

for test_case in range(1, T+1):
    # N은 상자의 개수, Q는 작업의 개수
    N, Q = map(int, input().split())
    work = [list(map(int, input().split())) for _ in range(Q)]
    box = [0]*N         # 박스 0으로 초기화

    for i in range(Q):  # 작업 횟수만큼 반복
        L = work[i][0]  # 범위 받아 오기
        R = work[i][1]

        for j in range(L, R+1):     # L부터 R까지
            box[j-1] = i+1          # L은 1부터 시작하므로 인덱스는 -1
                                    # i는 0부터 시작하므로 1부터 넣어주게 1을 더한다.
    print(f'#{test_case}', *box)