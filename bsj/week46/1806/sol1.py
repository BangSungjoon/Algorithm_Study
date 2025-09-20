# [백준] 부분합
n, s = map(int, input().split())
li = list(map(int, input().split()))
answer = n + 1
point1 = 0
current_sum = 0

for point2 in range(n):
    current_sum += li[point2]
    while current_sum >= s:
        current_sum -= li[point1]
        answer = min(answer, point2 - point1 + 1)
        point1 += 1

if answer == n + 1:
    print(0)
else:
    print(answer)