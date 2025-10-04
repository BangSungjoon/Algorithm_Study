# [백준] 덱
import sys
from collections import deque
input = sys.stdin.readline
deck = deque()
for _ in range(int(input())):
    order = input().strip()
    if order == 'pop_front':
        print(deck.popleft() if deck else -1)
    elif order == 'pop_back':
        print(deck.pop() if deck else -1)
    elif order == 'size':
        print(len(deck))
    elif order == 'empty':
        print(0 if deck else 1)
    elif order == 'front':
        print(deck[0] if deck else -1)
    elif order == 'back':
        print(deck[-1] if deck else -1)
    else:
        o, x = order.split()
        if o == 'push_front':
            deck.appendleft(x)
        else:
            deck.append(x)