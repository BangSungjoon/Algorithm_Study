from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0

    bridge = deque([0] * bridge_length)  # 현재 다리 상태
    current_weight = 0  # 현재 다리에 올라간 트럭들 무게

    while bridge:
        time += 1

        # 다 건넌 트럭 빼주기(트럭이 건너는 중이면 빈 공간 빼주기)
        truck = bridge.popleft()
        current_weight -= truck

        # 대기 트럭들이 남아있으면 bridge에 올리는 작업 진행
        if truck_weights:
            if current_weight + truck_weights[-1] <= weight:
                next_truck = truck_weights.pop()  # 다음 건널 트럭
                bridge.append(next_truck)  # 다리에 올리고
                current_weight += next_truck  # 무게도 추가
            else:
                bridge.append(0)  # bridge 길이는 유지해야 하니 0을 넣어줌

    return time