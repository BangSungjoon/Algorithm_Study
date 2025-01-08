# [D3] 5789 현주의 상자 바꾸기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # N : 박스 수 Q : 숫자 입력 횟수
    N, Q = map(int, input().split())
    arr = [0] * (N+1)                   # 출력시 인덱스 주의

    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            arr[i] = q
    
    print(f'#{t}', end=' ')
    print(*arr[1:])