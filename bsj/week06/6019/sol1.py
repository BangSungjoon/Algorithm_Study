# 기차 사이의 파리
T = int(input())

for test_case in range(1, T+1):
    # D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력, B는 기차 B의 속력, F는 파리의 속력
    D, A, B, F = map(int, input().split())

    hour = D / (A+B)    # 충돌까지 걸리는 시간
    # 충돌까지 걸리는 시간동안 파리가 이동한 거리 구해서 출력
    print(f'#{test_case} {F*hour}')