import sys
# from pprint import pprint
sys.stdin=open('input.txt')
# 1뒤에 2가오면 카운트

for tc in range(1,11):
    N=int(input()) 
    arr=[list(map(int,input().split()))for _ in range(N)] #N*N배열 받아옴
    count=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j][i]==1: #기준이 되는 빨강(나오는 순서대로)
                 for k in range(1, 100-j):  #기준인 빨강 뒤에것들 순회
                    if arr[j+k][i]==1:  # 다음것이 빨강이면 (for k 문 탈출)(전치행렬이므로 원래 내가쓰던 배열대로 조종)
                       break
                    elif arr[j+k][i]==2 : # 다음것이 파랑이면 COUNT+=1하고 탈출
                       count+=1
                       break

    print(f'#{tc} {count}')             