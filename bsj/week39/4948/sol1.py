arr = list(range(246913))
arr[1] = 0
for i in range(2, len(arr)):
    if arr[i]:
        cnt = 2
        while i * cnt < 246913:
            arr[i*cnt] = 0
            cnt += 1

while True:
    n = int(input())
    if n == 0:
        break

    result = n - arr[n+1:2*n+1].count(0)
    print(result)