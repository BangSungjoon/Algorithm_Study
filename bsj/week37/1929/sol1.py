# 소수 구하기
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
m, n = map(int, input().split())
arr = list(range(1, n+1))
visited = [0]*(n+1)
result = []
for i in arr:
    if i != 1 and visited[i] == 0:
        j = 2

        while i * j <= n:
            visited[i * j] = 1
            j += 1

        if i >= m:
            result.append(i)

for i in result:
    print(i)