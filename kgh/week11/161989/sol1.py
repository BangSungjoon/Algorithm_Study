
def solution(n, m, section):
    answer = 0
    current = 0  # 현재 페인트칠이 끝난 지점
    # 칠해야할 곳
    for start in section:
        # 페인트칠이 끝난 위치보다 더 뒤에 칠해야 할 데가 있으면
        if start > current:  # 페인트칠이 필요한 구역에 도착하면
            answer += 1
            current = start + m - 1  # 롤러 길이만큼 칠하고 끝나는 위치 갱신
            
    return answer

n = 8
m = 4
section = [2, 3, 6]
print(solution(n, m, section))