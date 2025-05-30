import sys, copy
input = sys.stdin.readline

N = int(input())
max_dp = [list(map(int, input().split())), [0] * 3] # 각 6칸
min_dp = [copy.deepcopy(max_dp[0]), [0] * 3]

# 입력할때 마다 dp 연산한다.
for i in range(1, N):
    x1, x2, x3 = map(int, input().split())
    
    # 최대값 dp 연산
    max_dp[1][0] = x1 + max(max_dp[0][0], max_dp[0][1])   # 이전 행의 0번째와 1번째 열의 최대값을 더함
    max_dp[1][1] = x2 + max(max_dp[0][0], max_dp[0][1], max_dp[0][2])
    max_dp[1][2] = x3 + max(max_dp[0][1], max_dp[0][2])
    
    # 최소값 dp 연산
    min_dp[1][0] = x1 + min(min_dp[0][0], min_dp[0][1])
    min_dp[1][1] = x2 + min(min_dp[0][0], min_dp[0][1], min_dp[0][2])
    min_dp[1][2] = x3 + min(min_dp[0][1], min_dp[0][2])
    
    # dp연산 끝난 후에 다시 
    # 이전값으로 저장
    max_dp[0] = copy.deepcopy(max_dp[1])
    min_dp[0] = copy.deepcopy(min_dp[1])
    
print(max(max_dp[0]), min(min_dp[0]))

# 배열을 두개만 할 수 있으니까 시간단축