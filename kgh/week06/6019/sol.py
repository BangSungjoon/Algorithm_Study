import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())
    print(f'#{tc} {F * D/(A+B)}')  # 두 기차가 부딪힐 때까지의 시간 * 파리의 속력