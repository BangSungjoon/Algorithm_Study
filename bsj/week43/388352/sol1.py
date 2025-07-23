def solution(n, q, ans):
    # 1부터 n까지의 수로 5자리 암호문
    li = [] # 모든 조합
    def dfs(arr, idx):
        if len(arr) == 5:
            li.append(arr[:])
            return
        for i in range(idx, n+1):  # 다음 숫자부터만 탐색
            arr.append(i)
            dfs(arr, i+1)      # i+1로 다음 숫자 제한
            arr.pop()
    dfs([], 1)
    answer = 0
    
    for check in li:
        possible = True
        for i in range(len(q)):
            cnt = 0
            for c in check:
                if c in set(q[i]):
                    cnt += 1

            if cnt != ans[i]:
                possible = False
                break
                
        if possible:
            answer += 1
    return answer