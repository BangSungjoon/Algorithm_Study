# 오큰수

# 입력부터 받자...
n = int(input())
arr = list(map(int, input().split()))

result = [0]*n # 정답
result[-1] = -1
idx = 0 # 오큰수의 index 값
value = 0 # 오큰수의 value
# n번 반복으로 arr 순회
for i in range(n-1):
    if i < idx:
        result[i] = value
    else:
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                value = arr[j]
                idx = j
                result[i] = value
                break
        if result[i] == 0:
            result[i] = -1

print(*result)