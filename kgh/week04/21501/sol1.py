import sys
sys.stdin = open('input.txt', 'r')

arr = list(range(1, 13))
M = len(arr)  # 12

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 2, 3
    cnt = 0
    for i in range(1 << M):  # 1*(2**12) : 0, 1, 2...,4095
        ss = []  #  임시 부분집합 생성을 위한 리스트
        for j in range(M):  # 12만큼 순회 : 0, 1, 2...,11
            if i & (1 << j):  # i와 1*(2**j)
                ss.append(arr[j])
        sum_ss = 0
        for s in ss:
            sum_ss += s
            
        if len(ss) == N and sum_ss == K:
            cnt += 1

    print(f'#{tc} {cnt}')
