# [백준] LCS2
s1 = input()
s2 = input()
n = len(s1)
m = len(s2)

# dp[i][j]: s1[i]번째 s2[j]번째 글자까지 LCS의 글자 수
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            # 같다면 이전의 LCS 길이에서 +1
            # 끝 글자가 같다는 뜻이니 두 문자열의 공통 이전을 봐야 함
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs = dp[n][m]
answer = ''
i, j = n, m
# 끝 글자부터 본다
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        # 두 글자가 일치한다면
        answer += s1[i-1]
        i -= 1
        j -= 1
    else:
        # 두 끝 글자가 일치하지 않는다면
        if dp[i-1][j] > dp[i][j-1]:
            # lcs가 더 긴쪽으로 이동
            i -= 1
        else:
            j -= 1

print(lcs)
print(''.join(reversed(answer)))