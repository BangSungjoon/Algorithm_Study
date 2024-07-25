T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    min_sum = sum(N_list[0:0 + M])
    max_sum = 0

    for i in range(N-M+1):
        num = sum(N_list[i:i+M])

        if min_sum > num:
            min_sum = num
        if max_sum < num:
            max_sum = num

        answer = max_sum - min_sum

    print(f'#{test_case} {answer}')