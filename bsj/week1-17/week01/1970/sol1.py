T = int(input())

for testcase in range(1,T+1):
    money_list=[50000, 10000, 5000, 1000, 500, 100, 50, 10]
    N = int(input())
    result = []
    print(f'#{testcase}')

    for i in money_list:
        result.append(N//i)
        N %= i
    print(*result)
