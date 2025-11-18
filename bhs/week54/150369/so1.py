def solution(cap, n, deliveries, pickups):

    d = list(deliveries)
    p = list(pickups)
    answer = 0

    # 전체 남은 박스가 없을 때까지 반복
    while sum(d) > 0 or sum(p) > 0:
        # 가장 멀리 가야 하는 집 찾기 (뒤에서부터)
        farthest = 0
        for i in range(n - 1, -1, -1):
            if d[i] > 0 or p[i] > 0:
                farthest = i + 1
                break

        # 왕복 거리 더하기
        answer += farthest * 2

        # 배달
        for _ in range(cap):
            idx = farthest - 1
            found = False
            while idx >= 0:
                if d[idx] > 0:
                    d[idx] -= 1
                    found = True
                    break
                idx -= 1
            if not found:
                break

        # 수거: 동일하게 한 박스씩, 박스마다 탐색
        for _ in range(cap):
            idx = farthest - 1
            found = False
            while idx >= 0:
                if p[idx] > 0:
                    p[idx] -= 1
                    found = True
                    break
                idx -= 1
            if not found:
                break

    return answer
