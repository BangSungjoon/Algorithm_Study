import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    len_num = N//4  # 한토막 길이
    lst = []
    for _ in range(N):
        for i in range(0, N, len_num):
            if num[i:i+len_num] not in lst:  # 중복 검사
                lst.append(num[i:i+len_num])
        num = num[-1] + num[:-1]  # 뚜껑 돌리기
    answer = int(sorted(lst, reverse=True)[K-1], 16)  # 16진수를 10진수로 변환
    print(f'#{tc} {answer}')