from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)

    target = (q1_sum + q2_sum) / 2

    max_try = len(q1) * 3  # q1의 길이의 2배 만큼 시도하면 q1과 q2 바뀜, 3배만큼 하면 q1이 다시 원래대로 돌아옴

    cnt = 0

    # 타겟합보다 큰 큐에서 빼서 작은 큐에 넣는다
    while cnt < max_try:
        if q2_sum > target:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
            cnt += 1
        elif q1_sum > target:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
            cnt += 1

        if q1_sum == target and q2_sum == target:
            break

    if cnt == max_try:
        cnt = -1

    return cnt