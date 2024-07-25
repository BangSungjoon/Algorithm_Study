T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr=[]
    for i in range(N):
        arr.append(list(map(int, input().split())))
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_kill = 0
            for k in range(M):
                for t in range(M):
                    fly_kill += arr[i+k][j+t]

            if max_kill < fly_kill:
                max_kill = fly_kill

    print(f'#{test_case} {max_kill}')