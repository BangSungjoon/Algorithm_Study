# [D2] 1945 간단한 소인수분해

import sys
sys.stdin = open('input.txt', 'r')

# 소수 리스트
prime = [2, 3, 5, 7, 11]

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    answer = [0] * 5    # 2의 지수, 3의 지수, ..., 11의 지수를 담을 list

    for i in range(len(prime)):
        while N % prime[i] == 0:    # 소수로 나누어 떨어지면,
            N /= prime[i]           # N 갱신
            answer[i] += 1          # prime 횟수 증가
    
    print(f'#{t}', end=' ')
    print(*answer)