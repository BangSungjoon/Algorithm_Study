# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    bus_stop_number = list(map(int, input().split()))

    current = 0     # 현재위치 0부터 시작
    charge_count = 0        # 충전횟수 0부터 시작

    while current + K < N:      # 최대 이동할 수 있는 값이 정류장 수보다 작을때
        next_stop = current + K     # 다음 정류장은 현재위치에서 K를 더한 값
        possible_chargers = [c for c in bus_stop_number if current < c <= next_stop]        # 충전가능한 구역(다음 정류장 사이에 있는 충전소 반복)

        if not possible_chargers:       # 충전소가 없다면
            charge_count = 0            # 도착 실패
            break

        current = max(possible_chargers)    # 충전가능한 곳들 중에 최댓값
        charge_count += 1       # 한번씩 최대값이 나올 때마다 충전 횟수 증가

    print(f'#{tc} {charge_count}')