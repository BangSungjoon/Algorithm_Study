def solution(triangle):
    # 바닥에서 위로 올라갈게
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            # 현위치 기준 아래 칸 두개 중 큰 값 합칠게
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    # 삼각형 꼭대기 = 최대 경로의 합
    return triangle[0][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))