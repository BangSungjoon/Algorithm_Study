A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())
LCS = [[""]*len(B) for _ in range(len(A))]


# LCS[i][j]는 A의 i번째까지의 문자열과
# B의 j번째까지의 문자열의 LCS 길이 값을 의미함
# LCS[i][j]에서, 만약 A[i] == B[j]라면
# 그 두 문자를 제외한 i-1개, j-1개의 LCS
# 만약 다르다면, i-1개, j개와 i개, j-1개
# 일 때의 LCS 중 큰 값 취하기. i-1개, j-1개
# 는 어차피 저 두 케이스보다 반드시 작거나 같으므로
# 두 케이스만 고려.
# 그런데 LCS 리스트 원소 값이 LCS 길이 값을 의미하므로,
# 원소를 LCS 문자열 자체로 둬도 됨. 그럼 길이 값도 갖고
# 최단 경로도 갖고 있게 됨.
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else: # 현재 문자가 같으면 -> 둘 다 한칸 전으로 이동한 LCS에서 현재 문자 추가, 다르면 두가지 경우 중 더 킨 LCS 문자열을 선택택
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

# result = LCS[-1][-1]
# # print(len(result), result, sep="\n")
# print(len(result))
# if result:  # 공통 부분 수열이 존재할 때만 출력
#     print(result)



# A = [""] + list(input().rstrip())
# B = [""] + list(input().rstrip())
# dp = [[0] * len(B) for _ in range(len(A))]

# for i in range(1, len(A)):
#     for j in range(1, len(B)):
#         if A[i] == B[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(LCS[-1][-1])
