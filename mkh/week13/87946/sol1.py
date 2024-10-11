from collections import deque


def solution(k, dungeons):
    # (피로도, 방문한 던전)을 담을 큐 q
    q = deque()
    n = len(dungeons)
    # 초기값 설정. 던전들을 순회하면서 만약 내가 갈 수 있는 던전이면 q에다 담아서 거기서부터 순회할거임.
    for i in range(n):
        if k >= dungeons[i][0]:
            q.append((k-dungeons[i][1], [i]))
    # 돌 수 있는 던전의 최대길이 변수 max_len
    max_len = 0
    
    # q에서 갈 수 있는 경우의 수가 있는 동안
    while q:
        piro, visited = q.popleft()
        # 여태까지 방문한 곳들의 개수가 크면 갱신
        if max_len < len(visited):
            max_len = len(visited)
        # 방문하지 않은 던전들을 돌면서 갈 수 있는 곳이 있다면 q에 더해준다.
        for i in range(n):
            if i not in visited and piro >= dungeons[i][0]:
                q.append((piro-dungeons[i][1], visited+[i]))

    return max_len


print(solution(80, [[80,20],[50,40],[30,10]]))
