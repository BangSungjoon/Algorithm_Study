# 백준 LCS
s1 = input()
s2 = input()
dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
"""
dp[i][j]는
문자열 s1의 앞에서부터 i번째 문자까지 s1[0:i]
문자열 s2의 앞에서부터 j번째 문자까지 s2[0:j]
이 둘의 LCS의 길이를 의미한다.
"""
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(s1)][len(s2)])