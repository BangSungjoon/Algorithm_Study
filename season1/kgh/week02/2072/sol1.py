import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스 개수 input
for test_case in range(1, T + 1):
    sum = 0
    # 테스트케이스 한줄씩 input 받아서 int로 list화
    nums = list(map(int, input().split()))
    for num in nums:
        # 짝수가 아니면
        if num % 2 != 0:
            sum += num # sum에 더하기
    print(f'#{test_case} {sum}')