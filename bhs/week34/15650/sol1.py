N, M = map(int, input().split())
ans = []

# n : 선택된 원소의 개수, s: 선택할 숫자 시작점
def dfs(n, s, lst) :
    # 종료 조건
    if n == M : # n이 M개가 될때
        ans.append(lst) 
        return
    
    # 재귀 호출
    for i in range(s, N+1) :
        dfs(n+1, i+1, lst + [i]) # lst에 원소를 추가하여 오름차순으로

dfs(0, 1, [])
for lst in ans :
    print(*lst)