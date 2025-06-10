def dfs(adj_l, current, visited):
    cnt = 1
    for ad in adj_l[current]:
        if visited[ad] == 0:
            visited[ad] = 1
            cnt += dfs(adj_l, ad, visited)
    return cnt

def solution(n, wires):
    answer = n
    
    # 반복문을 돌며 전부 끊어보기
    for i in range(len(wires)):
        arr = wires[:]
        arr.pop(i)
        
        # 인접 리스트 만들기
        adj_l = [[] for _ in range(n+1)]
        for i in range(len(arr)):
            adj_l[arr[i][0]].append(arr[i][1])
            adj_l[arr[i][1]].append(arr[i][0])
        
        visited = [0]*(n+1)
        results = []
        
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                result = dfs(adj_l, i, visited)
                results.append(result)
        
        gap = abs(results[0] - results[1])
        answer = min(answer, gap)
        
    return answer