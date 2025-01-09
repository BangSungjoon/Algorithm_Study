# 6485 삼성시의 버스 노선

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input())    # 버스 노선 수

    # 버스 노선 리스트 만들기 
    routes = [0] * N
    for i in range(N):
        # [Ai, Bi] routes에 추가
        # Ai : 버스 노선이 시작되는 정류장 번호, Bi : 버스 노선이 끝나는 정류장 번호 
        routes[i] = list(map(int, input().split())) 

    C = int(input())    # 정류장 수

    # 정류장 리스트 만들기
    stops = [0] * C
    for i in range(C):
        stops[i] = int(input())
    
    answer = [0] * C

    # 노선 순회 -> 정거장 순회 
    for route in routes:
        for i in range(C):
            if route[0] <= stops[i] <= route[1]:   # 정류장이 노선 안에 포한된다면,
                answer[i] += 1                  # 현재 버스정류장을 포함하는 노선 추가
    
    print(f'#{t}', end=' ')
    print(*answer)