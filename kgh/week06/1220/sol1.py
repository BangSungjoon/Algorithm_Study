import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    answer = 0
    for i in range(N):
        tmp = ''
        for j in range(N):
            if arr[j][i] != '0':
                tmp += arr[j][i]
        answer += tmp.count('12')
    print(f'#{tc} {answer}')
