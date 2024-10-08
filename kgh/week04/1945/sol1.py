import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    primes = [2, 3, 5, 7, 11] # 소수 리스트
    counts = [0] * len(primes) # 소수별 개수 카운트

    for i in range(len(primes)):
        while N % primes[i] == 0:
            counts[i] += 1
            N //= primes[i]
    print(f'#{test_case}', *counts)