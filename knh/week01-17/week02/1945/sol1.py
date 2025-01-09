# 1945 간단한 소인수분해

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스
T = int(input())

for t in range(1, T+1) :
    N = int(input())

    # 2의 지수, 3의 지수, ..., 11의 지수 0으로 초기화
    # index 접근
    powers = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0}
    
    prime_numbers = [2, 3, 5, 7, 11]

    # N을 소수로 나누기
    # prime_numbers 에 들어있는 소수 꺼내오기
    for i in range(len(prime_numbers)) :
        # 소수로 나누어 떨어지면 딕셔너리 powers 소수에 해당하는 key의 value 값 증가
        while N % prime_numbers[i] == 0 :
            powers[prime_numbers[i]] += 1
            # N 값 소수로 나누기
            N = N / prime_numbers[i]

    answer = ' '.join(list(map(str, powers.values())))

    # 출력
    print(f'#{t} {answer}')