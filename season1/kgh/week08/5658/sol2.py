import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    len_num = N//4  # 한토막 길이
    numbers = set()
    for _ in range(len_num):  # 회전하기 위한 반복문
        for i in range(0, N, len_num):  # 토막 내기 위한 반복문
            numbers.add(num[i:i+len_num])  # numbers set에 추가
        num = num[-1] + num[:-1]  # 뚜껑 돌리기
    # 내림차순 정렬 후 K번째 요소를 10진수로 변환
    answer = int(sorted(numbers, reverse=True)[K-1], 16)
    print(f'#{tc} {answer}')