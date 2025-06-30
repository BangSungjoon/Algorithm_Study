# 백준 제로
k = int(input())
result = []

for _ in range(k):
    num = int(input())
    if num == 0:
        if result:
            result.pop()
    else:
        result.append(num)

print(sum(result))