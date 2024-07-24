# 2072 홀수만 더하기

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 입력
T = int(input())

for t in range(1, T+1) :
    # 입력 받기
    numbers = list(map(int, str(input()).split()))

    # 홀수의 합을 저장할 변수
    sum = 0

    # 숫자 순회
    for num in numbers :
        # 2로 나누었을 때 나머지가 1인 수 찾기
        if num % 2 == 1:
            sum += num
    
    print(f'#{t} {sum}')
