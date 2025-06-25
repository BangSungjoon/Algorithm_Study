# 백준 집합
# Trouble Shooting
# 1. 입력이 엄청나게 많은 테스트 케이스가 있어서, sys.stdin.readline을 사용했다.
# 2. 입력의 개행문자를 제거하기 위해 strip을 사용했다.
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    text = input().strip()  # 개행문자를 제거하기 위해 strip을 사용해야 한다.
    if 'all' == text:
        s = {x for x in range(1, 21)}
    elif 'empty' == text:
        s = set()
    else:
        order, num = text.split()
        num = int(num)

        if order == 'add':
            s.add(num)
        elif order == 'remove':
            if num in s:
                s.remove(num)
            else:
                continue
        elif order == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)