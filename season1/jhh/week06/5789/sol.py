import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    input_lst = [list(map(int, input().split())) for _ in range(Q)]
    new_lst = [0] * (N)
    for i in range(Q):
        for j in range(input_lst[i][0]-1, input_lst[i][1]):
            new_lst[j] = i+1
    print(f'#{tc}', *new_lst)

