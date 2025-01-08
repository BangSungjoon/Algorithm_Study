import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    # 숫자가 나오면, True로 업데이트하기 위한 False 집합
    check_num = [False] * 10
    k = 0
    # 모든 요소가 True가 될 때까지 반복
    while not all(check_num):
        k += 1  # 배수 k를 1씩 증가시킴
        current_N = k * N  # 현재 N = N * k 로 업데이트

        for num in str(current_N):
            # 각 num을 통해 인덱스로 접근
            check_num[int(num)] = True
        # 결과 출력
    print(f'#{test_case} {current_N}')