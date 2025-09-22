def solution(cap, n, deliveries, pickups):
    answer = 0

    # 처리해야 할 배달/수거 상자 수를 나타내는 변수
    deliver_need = 0
    pickup_need = 0

    # 가장 먼 집부터 역순으로 확인
    for i in range(n - 1, -1, -1):

        # i번째 집에 들렀을 때, 해당 집에 쌓이는 배달/수거량을 누적
        deliver_need += deliveries[i]
        pickup_need += pickups[i]

        # 만약 i번째 집까지의 누적 배달/수거량이 하나라도 양수라면 이 집을 방문
        while deliver_need > 0 or pickup_need > 0:
            # i번째 집까지는 무조건 와야 하므로 왕복 거리를 더함
            answer += (i + 1) * 2

            # 트럭이 한 번 왕복하면 cap만큼의 배달/수거 용량이 생김
            # 누적된 필요량에서 cap만큼을 빼줌
            deliver_need -= cap
            pickup_need -= cap

    return answer