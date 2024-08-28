def backtrack(row, current_sum):
    global min_sum

    # 가지치기 : 현재 합이 이미 최소 합보다 크다면 종료
    if current_sum >= min_sum:
        return

    # 모든 행에서 숫자를 골랐다면 min_sum값 갱신
    if row == N:
        # 모든 행에서 숫자를 다 선택한 경우, 합 비교 후 갱신
        min_sum = min(min_sum, current_sum)
        return

    # 현재 행에서 하나의 숫자 선택
    for col in range(N):
        if not visited[col]:  # 아직 선택되지 않은 열이라면
            visited[col] = True  # 방문 표시
            backtrack(row+1, current_sum + arr[row][col])
            visited[col] = False  # 백트래킹 위해 초기화화

# 실행
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_sum = 1000  # 최소값을 구하기 위한 임의의 매우 큰 값 할당

    backtrack(0, 0)
    print(f'#{tc} {min_sum}')