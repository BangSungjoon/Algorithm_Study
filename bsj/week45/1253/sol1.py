# [백준] 좋다
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
answer = 0

for i in range(n):
    point1 = 0
    if point1 == i:
        point1 += 1
    point2 = n - 1
    if point2 == i:
        point2 -= 1
    while 0 <= point1 < point2 < n:
        total = arr[point1] + arr[point2]
        if total == arr[i]:
            answer += 1
            break
        elif total < arr[i]:
            point1 += 1
            if point1 == i:
                point1 += 1
        elif total > arr[i]:
            point2 -= 1
            if point2 == i:
                point2 -= 1

print(answer)