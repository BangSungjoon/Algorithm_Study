# 최소 힙
# 연산의 개수 n
# n개의 정수 x
import heapq

li = []
result = []
for _ in range(int(input())):
    x = int(input())

    if x == 0:
        if not li:
            # print(0)
            result.append(0)
        else:
            # print(heapq.heappop(li))
            result.append(heapq.heappop(li))
    else:
        heapq.heappush(li, x)

for i in range(len(result)):
    print(result[i])