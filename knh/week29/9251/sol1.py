# [G5] 9251 LCS

s1 = input().strip()
s2 = input().strip()

lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]   # LCS 기록할 배열

for x in range(1, len(s1) + 1):
    for y in range(1, len(s2) + 1):
        if s1[x-1] == s2[y-1]:
            lcs[x][y] = lcs[x-1][y-1] + 1
        else:
            lcs[x][y] = max(lcs[x-1][y], lcs[x][y-1])

print(max(map(max, lcs)))