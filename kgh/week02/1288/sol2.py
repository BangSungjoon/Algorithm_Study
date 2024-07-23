import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = set() # 숫자 set 생성
    # 배수
    k = 0
    # 숫자 set의 길이가 0~9 총 10개가 될 때까지 반복
    while len(nums) < 10:
        k += 1  # 배수 k를 1씩 증가시킴
        current_N = N * k  # 현재 N = N * k 로 업데이트
        nums.update(str(current_N))  # 숫자 set에 str로 update

        # 결과 출력
    print(f'#{test_case} {current_N}')