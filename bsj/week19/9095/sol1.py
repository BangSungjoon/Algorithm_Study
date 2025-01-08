# 백준
# 1, 2, 3 더하기
def dp(current):        # dp로 풀고 싶었는데 결국 DFS이다. 이게 DP인건가..?
    global result, n
    if current == n:    # 현재의 합이 n과 같아진다면
        result += 1     # 정답 +1
        return

    for i in range(1, 4):       # 1부터 3까지 돌아버려
        if current + i <= n:    # 현재값 + (1~3)이 목표숫자를 넘는거 아니라면
            dp(current + i)     # 다음으로 진행시켜

T = int(input())        # 테스트 케이스의 개수
for _ in range(T):
    n = int(input())    # 목표 숫자
    result = 0          # 정답 초기값

    for k in range(1, 4):
        dp(k)
    print(result)