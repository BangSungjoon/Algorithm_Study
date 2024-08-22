# 1219. 길찾기
for _ in range(10):
    # test_case와 길의 개수 N 입력 받기
    test_case, N = map(int, input().split())
    result = 0  # 가능 여부

    # 순서쌍 입력 받기
    arr = list(map(int, input().split()))

    # 인접 리스트 만들기
    adj_l = [[] for _ in range(100)]
    for i in range(N):
        a = arr[i*2]
        b = arr[i*2+1]
        adj_l[a].append(b)

    # 큐 만들기, 시작점 방문 표시
    queue = []
    visited = [0]*100
    queue.append(0)
    visited[0] = 1

    while queue:
        t = queue.pop(0)

        if t == 99:  # 목적지에 도착한 경우
            result = 1
            break

        for w in adj_l[t]:
            if visited[w] == 0:     # 방문한 적이 없다면
                queue.append(w)
                visited[w] = 1

    print(f'#{test_case} {result}')
