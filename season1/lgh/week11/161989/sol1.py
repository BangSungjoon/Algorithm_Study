# 덧칠 하기
def solution(n, m, section):
    now = 0 # 현재 구역 인덱스
    i = 1   # 비교할 구역 인덱스
    paint = 1 #페인트는 한번 칠하고 시작
    while now < len(section) and i < len(section): # section리스트의 인덱스범위에서 반복
        if section[i] - section[now] < m: # 비교할 구역-현재구역이 m보다 작으면 비교할구역의 인덱스 늘림
            i += 1
        elif section[i] - section[now] >= m: #비교할 구역-현재구역이 m보다 크거나 같으면 
            paint += 1 #페인트칠 횟수늘리고
            now = i  # 현재 위치를 비교했던 구역값으로 갱신
            i += 1  #비교할 구역 인덱스를 늘려줌
    return paint