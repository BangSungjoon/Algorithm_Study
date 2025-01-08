# [D3] 4831 전기버스

T = int(input())

for t in range(1, T+1):
    # 입력 받기
    K, N, M = map(int, input().split())     # K : 한번 충전할 때 갈 수 있는 거리, N : 총 길이, M : 정류장 위치
    stop = list(map(int, input().split()))    # 버스 정류장 위치 저장 변수

    # 사용할 변수
    move = K        # 현재 이동할 수 있는 거리 저장 변수
    position = 0    # 현재 위치 저장 변수
    stop_idx = 0    # 버스 정류장 위치 리스트를 탐색할 때 사용할 인덱스
    cnt = 0         # 충전 회수 저장 변수

    # 길 끝까지 도착할 때까지 탐색
    while position < N+1:
        if position == stop[stop_idx]:  # 지금 위치에 정류장이 있다면
            if stop_idx == len(stop) -1:    # 마지막 정류장이라면
                if N - position > move:     # 끝까지 갈 수 없는 상황이라면
                    move = K   # 충전해라
                    cnt += 1    # 충전횟수 늘려라
            elif move == 0 or stop[stop_idx+1] - position > move: # 더 이상 갈 수 없거나, 다음 정류장까지 갈 수 없는 상태면
                move = K   # 충전해라
                cnt += 1    # 충전횟수 늘려라
            if stop_idx+1 < len(stop):  # stop 마지막까지 탐색한게 아니면
                stop_idx+=1             # stop_idx 증가
        if move == 0 and position != N:    # 더 이상 진행할 수 없고 끝까지 온게 아니라면
            cnt = 0
            break
        position += 1  # 다음 칸으로 이동
        move -= 1  # 연료 하나 닳게

    # 출력
    print(f'#{t} {cnt}')