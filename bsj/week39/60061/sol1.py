def check(answer):
    """
    설치 혹은 삭제가 가능한지 검사하는 함수
    일단 냅다 설치 또는 삭제를 한 후, answer를 돌면서 설치가 가능했는지 검사
    """
    for x, y, a in answer:
        if a == 0:  # 기둥이라면
            if (
                y == 0 or   # 바닥 위에 있으면 가능
                [x, y-1, 0] in answer or    # 아래에 기둥이 있었다면 가능
                [x-1, y, 1] in answer or    # 왼쪽에 보가 있었다면 가능
                [x, y, 1] in answer         # 현재 위치에 보가 있다면 가능
            ):
                continue    # 조건 하나라도 만족하면 기둥 설치 가능
            return False    # 위 조건이 모두 아니라면 설치 불가
        else:      # 보라면
            if (
                [x, y-1, 0] in answer or    # 왼쪽 끝이 기둥 위에 있으면 가능
                [x+1, y-1, 0] in answer or  # 오른쪽 끝이 기둥 위에 있으면 가능
                [x-1, y, 1] in answer and [x+1, y, 1] in answer # 양쪽 끝이 보와 연결되어 있다면 가능
            ):
                continue    # 조건 하나라도 만족하면 기둥 설치 가능
            return False    # 위 조건이 모두 아니면 설치 불가
    return True     # 모든 구조물이 조건을 만족하면 True

def solution(n, build_frame):
    # build_frame의 [x, y, a, b]
    # x, y: 설치 좌표
    # a: 설치 또는 삭제할 구조물의 종류, 0은 기둥, 1은 보
    # b: 구조물을 설치할 지, 혹은 삭제할 지 0은 삭제, 1은 설치
    answer = []
    arr = [[0]*(n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1:  # 설치의 경우, 일단 설치 후 검사 받기
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:   # 제거의 경우, 일단 제거 후 검사 받기
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return answer