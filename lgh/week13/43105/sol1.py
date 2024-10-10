# 정수 삼각형 43105

def solution(triangle):
    max_triangle = [[0] * len(triangle) for _ in range(len(triangle))] # max_triangle은 최댓값을 넣어줄 배열
    max_triangle[0][0] = triangle[0][0] # max_triangle에 시작값 넣기

    for i in range(1, len(triangle)):
        for j in range(i + 1): # 열 개수는 (해당 행+1) 개
            if j == 0: # 맨 왼쪽 계산
                max_triangle[i][j] = max_triangle[i - 1][j] + triangle[i][j]  
            elif j == i: # 맨 오른쪽 계산
                max_triangle[i][j] = max_triangle[i - 1][j - 1] + triangle[i][j]
            else: # 중간값은 오른쪽 위의 값 또는 왼쪽 위의 값 중 큰 값을 더해줌
                max_triangle[i][j] = max(max_triangle[i - 1][j - 1], max_triangle[i - 1][j]) + triangle[i][j] # 윗값의 최댓값 + 아래쪽 원래값

    answer = max(max_triangle[len(triangle) - 1]) # 마지막행에서 최댓값이 정답
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))