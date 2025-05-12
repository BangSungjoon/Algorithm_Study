def dfs(idx, li):
    # 조합 길이가 m과 같아지면 복사본을 저장
    if len(li) == m:
        result.append(li.copy())
        return

    for i in range(idx, n+1):
        li.append(i)
        dfs(i+1, li)
        li.pop()

n, m = map(int, input().split())
result = []
dfs(1, [])

for re in result:
    print(*re)
