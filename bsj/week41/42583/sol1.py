from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)     # 다리 상태를 나타내는 큐
    truck_weights = deque(truck_weights)  # 대기 트럭 큐
    total_weight = 0                      # 현재 다리 위의 총 무게
    time = 0

    while bridge:
        time += 1
        # 다리에서 나가는 트럭(혹은 빈 자리)
        out = bridge.popleft()
        total_weight -= out

        # 새 트럭 진입 가능한지 검사
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                # 현재 무게 + 진입할 트럭 무게가 다리가 견딜 수 있는 무게 보다 작다면
                t = truck_weights.popleft()
                bridge.append(t)
                total_weight += t
            else:
                # 새 트럭이 진입이 불가능 하다면 0을 추가
                bridge.append(0)
    return time