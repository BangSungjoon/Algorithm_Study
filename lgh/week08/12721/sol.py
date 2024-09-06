import sys
sys.stdin=open('input.txt')
# 파리퇴치3  12712
T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #대각선의 델타
    dx1 = [-1, -1, +1, +1]
    dy1 = [-1, +1, -1, +1]
    #십자가의 델타
    dx2 = [-1, 0, +1, 0]
    dy2 = [0, +1, 0, -1]
    ans = 0   #내가 구하고자하는 값
    max_lst = []  #+합과 x합 비교해서 큰 값을 max_lst에 넣어줌
    for i in range(N): #전체 배열 순회
        for j in range(N):
            cross_sum = arr[i][j]  # cross_sum의 기준값 정해줌(본인)(가운뎃값)   x
            plus_sum = arr[i][j]   # plus_sum의 기준값 정해줌(본인)(가운뎃값)    +
            for k in range(4): # 델타값 순회
                for m in range(1, M): # 기준칸으로부터 몇칸 갈 수 있는 지 = M값 순회
                    if 0 <= i + dx1[k] * m < N and 0 <= j + dy1[k] * m < N: # 배열에서 벗어나지 않는 범위만 더해줌
                        nx1 = i + dx1[k] * m
                        ny1 = j + dy1[k] * m
                        cross_sum += arr[nx1][ny1]
                    if 0 <= i + dx2[k] * m < N and 0 <= j + dy2[k] * m < N:
                        nx2 = i + dx2[k] * m
                        ny2 = j + dy2[k] * m
                        plus_sum += arr[nx2][ny2]

            if cross_sum > plus_sum:  # 한 x값과 +값 비교하여 큰 걸 max_lst에 넣음
                max_lst.append(cross_sum)
            else:
                max_lst.append(plus_sum)

    ans = max(max_lst) #최댓값찾기
    print(f'#{tc} {ans}')