# 백준 1072 게임
# 게임 횟수: X
# 이긴 게임: Y (Z%)
# 형택 승률: Z 소수점은 버린다.
# 형택이는 앞으로 무조건 이긴다.
x, y = map(int, input().split())
z = (y * 100) // x  # 승률 계산 (소수점 버림, 부동소수점 주의할 것)

if z < 99:
    n = (z+1)*x - 100*y
    d = 99-z
    if n % d == 0:  # 소수점이 존재하지 않는다면 그대로 출력
        answer = n // d
    else:           # 소수점이 존재한다면 올림 처리(최소값이니깐)
        answer = n // d + 1
else:
    answer = -1

print(answer)