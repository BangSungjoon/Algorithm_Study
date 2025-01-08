# 농작물 수확하기

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 농장 크기
    arr = [list(map(int, input())) for _ in range(N)] # 농작물가치 배열
   
    total = 0
    for i in range(N):  #행 기준으로 봄
        if i <= N//2: # 행이 중간보다 작거나 같을 때
            for j in range(N//2-i, N-(N//2-i)): # 순회해야할 열 범위 
                total += arr[i][j]
        if  i > N//2:  # 행이 중간보다 클 때
            for j in range(i-N//2, N-(i-N//2)): # 순회해야할 열 범위
                total += arr[i][j]
    print(f'#{tc} {total}')