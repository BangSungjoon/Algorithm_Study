# [LV2] 250136 석유 시추
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(land):
    answer = 0
    h = len(land)
    w = len(land[0])
    visited = [[0] * w for _ in range(h)]

    # STEP 1. 석유덩어리 찾기
    for x in range(h):
        for y in range(w):
            if land[x][y] == 1:
                stack = [(x, y)]
                check = []
                cnt = 0

                while stack:
                    x, y = stack.pop()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1 and not visited[nx][ny]:
                            stack.append((nx, ny))
                            visited[nx][ny] = 1
                            cnt += 1
                            check.append((nx, ny))

                for tx, ty in check:
                    land[tx][ty] = cnt

    # STEP 2. 열 순회 -> 최대 시추량 계산
    for col in range(w):
        tmp = 0
        for row in range(h):
            if (row == 0 or land[row-1][col] == 0) and land[row][col] > 0:
                tmp += land[row][col]
        if answer < tmp:
            answer = tmp

    return answer

# land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
# print(solution(land)) # 9
land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land)) # 16
land = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0]]
print(solution(land)) # 11
land = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]
print(solution(land))