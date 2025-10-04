# [백준] 카드2
from collections import deque

cards = deque(range(1, int(input())+1))
while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards[0])