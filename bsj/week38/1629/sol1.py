# 백준 곱셈
# [Trouble Shooting] 거듭제곱을 직접 계산했더니 너무 오래 걸려서 시간 초과가 발생했다.
# - 분할정복을 함수로 구현해서 해결했다.
# - 분할정복을 하지 않고 거듭제곱을 직접한다면 곱셈을 b번 하니깐 O(b)이다.
# - 분할정복을 하면 b를 계속 반으로 나누기 때문에 O(log b)로 줄어든다.
# - a^8 = (a^4)^2 = ((a^2)^2)^2
# - 직접 계산했다면 7번이지만 분할정복을 사용하게 된다면 총 3번만 계산하게 됨.
def 분할정복(a, b, c):
    if b == 1:
        return a % c
    half = 분할정복(a, b // 2, c)
    if b % 2 == 0:  # b가 짝수라면
        return (half * half) % c
    else:
        return (half * half * a) % c

a, b, c = map(int, input().split())
print(분할정복(a, b, c))