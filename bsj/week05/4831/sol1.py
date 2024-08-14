T = int(input())  # 테스트 케이스의 수를 입력받음

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # K: 최대 이동 정류장 수, N: 종점 번호, M: 충전기가 설치된 정류장 수
    M_list = list(map(int, input().split()))  # 충전기가 설치된 정류장 번호를 리스트로 입력받음

    current = 0  # 현재 버스의 위치를 0번 정류장으로 초기화
    charges = 0  # 충전 횟수를 0으로 초기화

    i = 0  # M_list에서 현재 탐색 중인 정류장의 인덱스를 나타내는 변수
    possible = True  # 종점까지 도달할 수 있는지 여부를 판단하는 변수

    # 충전기 간 거리가 K보다 크면, 해당 구간은 도달할 수 없으므로 불가능한 경우로 처리
    for j in range(1, len(M_list)):
        if M_list[j] - M_list[j-1] > K:
            possible = False
            break

    # 출발지에서 첫 번째 충전기까지의 거리 또는 마지막 충전기에서 종점까지의 거리가 K보다 크면 도달 불가능
    if M_list[0] > K or (N - M_list[-1] > K):
        possible = False

    if possible:  # 종점까지 도달이 가능한 경우에만 충전 횟수를 계산
        while current + K < N:  # 현재 위치에서 K만큼 이동했을 때 종점에 도달하지 못하는 경우 반복
            last_bus = current  # 현재 위치를 last_bus에 저장
            # 현재 위치에서 K 내에 도달 가능한 가장 먼 충전기 정류장을 탐색
            while i < len(M_list) and M_list[i] <= current + K:
                last_bus = M_list[i]
                i += 1
            current = last_bus  # 탐색한 정류장으로 현재 위치를 업데이트
            charges += 1  # 충전 횟수 증가

    print(f'#{test_case} {charges}')  # 테스트 케이스 번호와 충전 횟수를 출력
