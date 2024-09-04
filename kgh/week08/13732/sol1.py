import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    start_i, start_j = -1, -1  # 첫 번째 '#'의 위치
    end_i, end_j = -1, -1  # 마지막 '#'의 위치

    # 1단계: 격자판에서 첫 번째와 마지막 '#'의 위치를 찾아서 경계 상자를 설정
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if start_i == -1:  # 첫 번째 '#'을 발견했을 때
                    start_i, start_j = i, j
                end_i, end_j = i, j  # 마지막 '#' 위치 갱신

    # 2단계: 경계 상자가 정사각형을 이루는지 확인
    side_length = end_i - start_i + 1  # 정사각형의 변의 길이 계산
    # 경계 상자가 정사각형인지 확인 (가로 길이와 세로 길이가 동일해야 함)
    if (end_j - start_j + 1) != side_length:
        print(f"#{tc} no")
        continue

    # 3단계: 경계 상자 내부가 모두 '#'로 채워져 있는지 확인
    is_square = True
    for i in range(start_i, start_i + side_length):
        for j in range(start_j, start_j + side_length):
            if arr[i][j] != '#':  # 내부에 '#'이 아닌 문자가 있으면 정사각형이 아님
                is_square = False
                break
        if not is_square:
            break

    # 4단계: 결과 출력
    result = "yes" if is_square else "no"
    print(f"#{tc} {result}")