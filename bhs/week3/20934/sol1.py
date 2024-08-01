import sys
sys.stdin = open('input.txt', 'r')

def position(initial_position, K):
    # 초기 확률 설정
    percent = [0, 0, 0]
    percent[initial_position] = 1

    # K번의 교환 수행
    for _ in range(K):
        new_percent = [0, 0, 0]
        # 왼쪽과 가운데 교환
        new_percent[0] += percent[1] * 0.5
        new_percent[1] += percent[0] * 0.5
        # 오른쪽과 가운데 교환
        new_percent[1] += percent[2] * 0.5
        new_percent[2] += percent[1] * 0.5
        # 교환되지 않은 경우
        new_percent[0] += percent[0] * 0.5
        new_percent[2] += percent[2] * 0.5
        
        percent = new_percent

    # 가장 높은 확률을 가진 위치 반환
    return percent.index(max(percent))

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    S, K = input().split()
    K = int(K)
    
    # 초기 위치 결정
    if S == "o..":
        initial_position = 0
    elif S == ".o.":
        initial_position = 1
    else:  # "..o"
        initial_position = 2
    
    result = position(initial_position, K)
    print(result)