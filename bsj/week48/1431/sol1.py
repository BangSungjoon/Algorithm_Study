# [백준] 시리얼 번호
n = int(input())
arr = [input() for _ in range(n)]
serial = [[0, 0, ''] for _ in range(n)]
num = '123456789'

for i in range(n):
    serial[i][0] = len(arr[i])
    sum_of_digits = 0
    for j in arr[i]:
        if j in num:
            sum_of_digits += int(j)
    serial[i][1] = sum_of_digits
    serial[i][2] = arr[i]

serial.sort()

for i in range(n):
    print(serial[i][2])