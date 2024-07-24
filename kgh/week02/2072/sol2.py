import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스 개수 input
for test_case in range(1, T + 1):
    nums = map(int, input().split()) # 한줄씩 받아서 int로 형변환
    # 리스트 컴프리헨션으로 홀수 필터 후 sum
    print(f'#{test_case} {sum([num for num in nums if num%2 != 0])}')