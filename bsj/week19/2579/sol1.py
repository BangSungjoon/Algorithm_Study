# 백준 계단 오르기
def dfs(idx, score, before):
    # idx: 현재 계단 칸
    # score: 현재 점수
    # before: 전에 한칸 올랐니? 맞으면 True
    global n, result
    # 백트래킹
    if not before:  # 전에 두칸 올라왔다면 -> 한칸, 두칸 올라가기 둘다 가능
                    # but, 이 조건이 없으면 오답이 나옴, 그런데 왜 오답인지 모르겠음
        if score < back_floor[idx]:     # 이전에 올랐던 기록보다 낮다면 가지치기
            return
        else:
            back_floor[idx] = score     # 이전 기록보다 높다면 점수 기록

    if idx == n-1 and score > result:     # 꼭대기 칸에 도달했고, 현재 점수가 최대 점수보다 높다면
        result = score
        return
    if before:              # 전에 한칸만 올랐었다면 무조건 두칸 올라가슈
        if idx+2 <= n-1:    # 범위 넘어가나 체크
            dfs(idx+2, score+floor[idx+2], False)
        else:               # 범위 넘었으면 나가리여
            return
    else:
        if idx+1 <= n-1:    # 한 칸만 올라가기
            dfs(idx+1, score+floor[idx+1], True)
        if idx+2 <= n-1:    # 두 칸 오르기
            dfs(idx+2, score + floor[idx+2], False)


n = int(input())    # 계단의 개수
floor = [0]*n       # 계단
for i in range(n):
    floor[i] = int(input())
result = 0          # 총 점수의 최댓값
back_floor= [0]*n

dfs(0, floor[0], False)
if n != 1:          # n이 1인 경우가 있어서 조건 추가
    dfs(1, floor[1], False)

print(result)