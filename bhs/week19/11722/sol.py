n = int(input())
list = list(map(int, input().split()))


sooyeol = [1]*n  # 숫자하나는 길이가 1이기때문에 1로 경로를 미리 만들어줌. sooyeol[i]는 길이가 됨 

for i in range(1, n):
    for j in range(i):
        if list[j] > list[i]:
            sooyeol[i] = max(sooyeol[i], sooyeol[j]+1) 

print(max(sooyeol))


# 그냥 작은 수를 찾는 수열
# list index out of range [0]*n
# 기존 수열에 더하는 거니까 sooyeol[j]+1 해야함