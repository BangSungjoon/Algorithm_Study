# PROGRAMMERS 코딩테스트 연습 > 동적계획법 > 정수 삼각형
# 43105
def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):    # 밑 바닥부터 올라와
        for j in range(len(triangle[i])):       # 각 칸 돌아보기
            # 각 칸은 아래에 깔고 앉은 놈 중 큰 놈이랑 더하기
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]                       # 꼭대기에 선 놈이 정점