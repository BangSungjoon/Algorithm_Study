def solution(numbers):
    answer = 0
    
    # dfs로 조합 만들기
    combination = set()
    
    def dfs(num, visited):
        if num:
            combination.add(int(num))
        
        for i in range(len(numbers)):
            if visited[i] == 0:
                visited[i] = 1
                dfs(num+numbers[i], visited)
                visited[i] = 0
            
    dfs('', [0]*len(numbers))
    
    # 소수 판별하는 체 만들기
    max_num = max(combination)
    arr = list(range(max_num+1))
    arr[1] = 0
    for i in range(2, max_num+1):
        if arr[i] == 0:
            continue
        cnt = 2
        while i*cnt <= max_num:
            arr[i*cnt] = 0
            cnt += 1
    
    decimal = set()
    for i in range(2, max_num+1):
        if arr[i]:
            decimal.add(arr[i])
            
    # 조합의 소수 판별
    for c in combination:
        if c in decimal:
            answer += 1
    
    return answer