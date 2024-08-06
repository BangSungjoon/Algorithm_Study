import sys
sys.stdin = open('input.txt', 'r')

arr = list(range(1, 13))
M = len(arr)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    bit = [0]*N
    cnt = 0
    for i in range(1 << M):
        ss = []
        for j in range(M):
            if i & (1 << j):
                ss.append(arr[j])
        sum_ss = 0
        for s in ss:
            sum_ss += s

        if len(ss) == N and sum(ss) == K:
            cnt += 1

    print(f'#{tc} {cnt}')
