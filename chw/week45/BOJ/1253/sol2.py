N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

cnt = 0

for i in range(len(num_list)):
    target = num_list[i]
    left = 0
    right = len(num_list) - 1

    # 투 포인터 탐색
    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        num = num_list[left] + num_list[right]

        if num < target:
            left += 1
        elif num > target:
            right -= 1
        else:
            cnt += 1
            break

print(cnt)