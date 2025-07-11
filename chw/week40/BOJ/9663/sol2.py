import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

def check(col):
    # i와 j는 행, col[i], col[j]는 열 -> i열을 기준으로 j열 순서대로 대각선 상에 있는지 검사
    for i in range(N):
        for j in range(i):

            # x1-x2 == y1-y2 면 대각선 상에 있음
            if abs(i - j) == abs(col[i] - col[j]):
                return False

    return True

cnt = 0
for col in permutations(range(N), N):
    if check(col):
        cnt += 1

print(cnt)