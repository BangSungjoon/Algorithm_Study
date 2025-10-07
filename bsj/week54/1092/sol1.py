# [백준] 배
n = int(input())    # 크레인의 수
limit = list(map(int, input().split())) # 크레인별 무게 제한
m = int(input())    # 박스의 수
boxes = list(map(int, input().split())) # 박스별 무게
cnt = 0     # 옮겨진 박스의 수
answer = 0

if max(boxes) > max(limit):
    print(-1)
    exit()

limit.sort(reverse=True)
boxes.sort(reverse=True)
visited = [0]*m
crane = [0]*n   # 크레인이 옮길 수 있는 box index
while cnt < m:
    for i in range(n):
        while crane[i] < m:
            if visited[crane[i]]:
                # 이미 옮겨진 박스라면 다음 박스 봐보자
                crane[i] += 1
            elif boxes[crane[i]] <= limit[i]:
                # 옮길 수 있는 박스라면 집고 다음 크레인으로 넘어가자
                visited[crane[i]] = True
                crane[i] += 1
                cnt += 1
                break
            else:
                # 옮길 수 없다면 더 가벼운 박스 보기
                crane[i] += 1
    answer += 1

print(answer)