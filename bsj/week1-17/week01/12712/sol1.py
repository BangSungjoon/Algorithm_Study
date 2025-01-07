T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    fly_arr = []

    for i in range(N):
        fly_arr.append(list(map(int, input().split())))

    plus_shape = 0
    x_shape = 0
    Max_sum = 0

    for i in range(N):
        for j in range(N):
            plus_shape = fly_arr[i][j]
            x_shape = fly_arr[i][j]
            for k in range(1, M):
                if j-k >= 0:
                    plus_shape += fly_arr[i][j-k]
                if j+k < N:
                    plus_shape += fly_arr[i][j+k]
                if i-k >= 0:
                    plus_shape += fly_arr[i-k][j]
                if i+k < N:
                    plus_shape += fly_arr[i+k][j]

                if i-k >= 0 and j-k >= 0:
                    x_shape += fly_arr[i-k][j-k]
                if i+k < N and j+k < N:
                    x_shape += fly_arr[i+k][j+k]
                if i-k >= 0 and j+k < N:
                    x_shape += fly_arr[i-k][j+k]
                if i+k < N and j-k >= 0:
                    x_shape += fly_arr[i+k][j-k]

                if Max_sum < plus_shape:
                    Max_sum = plus_shape
                if Max_sum < x_shape:
                    Max_sum = x_shape
    print(f'#{test_case} {Max_sum}')
