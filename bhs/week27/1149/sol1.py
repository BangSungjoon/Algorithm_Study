num = int(input())
rgb = []
ans = []

while(num != 0):
    temp = list(map(int,input().split()))
    rgb.append(temp)
    ans.append([0,0,0])

    num = num-1

ans[0] = rgb[0]

for i in range(1, len(ans)):
    for j in range(3):
        # 각 색상별로 이전 행의 다른 두 색상 중 최소 비용 선택
        if(j==0):
            # k=1, l=2 // 이거는 왜 컴파일 에러야?
            k=1
            l=2
        if(j==1):
            k=0
            l=2
        if(j==2):
            k=0
            l=1
         # 현재 색상의 최소 비용 계산
        ans[i][j] = min(rgb[i][j] + ans[i-1][k], rgb[i][j] + ans[i-1][l])

# 마지막 행의 최소 비용 출력
print(min(ans[len(ans)-1]))