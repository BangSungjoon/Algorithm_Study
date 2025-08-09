N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]

top = sum(costs)
bottom = max(costs)
ans = 0

while bottom <= top:
    amount = (top + bottom) // 2
    current = amount
    cnt = 1

    for cost in costs:
        # 현재 돈이 금액보다 더 많다면
        if current >= cost:
            current -= cost

        # 현재 돈보다 금액이 더 많다면
        elif current < cost:
            current = amount
            cnt += 1
            current -= cost

    # 예상보다 많이 뽑았으면 금액을 높이기
    if cnt > M:
        bottom = amount + 1
    # 예상보다 적게 뽑았으면 금액을 낮추기
    elif cnt <= M:
        ans = amount
        top = amount - 1

print(ans)