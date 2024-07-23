import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = input()
    k = 1
    num_list = []

    while len(num_list) < 10:
        current_N = int(N) * k
        k += 1
        for n in str(current_N):
            if n not in num_list:
                num_list.append(n)
    print(f'#{test_case} {current_N}')