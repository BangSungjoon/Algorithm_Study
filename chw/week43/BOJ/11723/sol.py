import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().split()

    if command[0] == 'add':
        num = int(command[1])
        S.add(num)

    elif command[0] == 'remove':
        num = int(command[1])
        S.discard(num)

    elif command[0] == 'check':
        num = int(command[1])
        print(1 if num in S else 0)

    elif command[0] == 'toggle':
        num = int(command[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    elif command[0] == 'all':
        S = set(range(1, 21))

    elif command[0] == 'empty':
        S = set()