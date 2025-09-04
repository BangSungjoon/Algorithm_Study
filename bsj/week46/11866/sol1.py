# [백준] 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
people = deque(list(range(1, n+1)))

answer = []

while people:
    people.rotate(-k+1)
    answer.append(people.popleft())

print('<' + ', '.join(map(str, answer)) + '>')