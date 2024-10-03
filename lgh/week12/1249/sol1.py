# 보급로

import sys 
sys.stdin=open('input.txt')

T =  int(input())
for tc in range(1, T+1):
    N = int(input())  # N은 지도크기
    arr = [list(map(int, input())) for _ in range(N)]

    
