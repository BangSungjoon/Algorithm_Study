import sys
sys.stdin = open('C:\\dev\\Algorithm\\2805\\input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range(N):
        if i <= N//2:
            for j in range(N//2-i, N//2+i+1):
                total += arr[i][j]
        else:
            for j in range(N//2-(N-i-1), N//2+(N-i)):
                total += arr[i][j]
    print(f'#{tc} {total}')

'''
N=5일 때
3 234 12345 234 3
2 123 01234 123 2

0 2
1 123
2 01234
3 123
4 2

N=7일 때
0 3
1 234 : N//2-i
2 12345
3 0123456

4 12345  : N//2  2 = N-i-1
5 234             1 = N-i-1
6 3
'''