# [백준] 사과 담기 게임
n, m = map(int, input().split())
j = int(input())
answer = 0
min_box = 1
max_box = m

for _ in range(j):
    apple = int(input())

    if apple > max_box:
        move = apple - max_box
        max_box = apple
        min_box += move
    elif apple < min_box:
        move = min_box - apple
        max_box -= move
        min_box = apple
    else:
        continue
    answer += move

print(answer)