def solution(name):
    answer = 0
    n = len(name)
    move = n - 1  # 초기 최대 이동 횟수 (모든 위치를 순차적으로 이동할 경우)

    for i in range(n):
        # 문자 변경 횟수 계산
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        # 다음 문자로 이동할 때의 최소 이동 거리 계산
        next = i + 1
        while next < n and name[next] == 'A':  # 연속된 A 건너뛰기
            next += 1

        # i 지점에서 앞으로 이동하는 거리와 뒤로 돌아가는 거리 비교
        move = min(move, i + n - next + min(i, n - next))
        # print(move)
        print(i + n - next + min(i, n - next))

    answer += move
    return answer
