import sys
sys.stdin=open('sample_input (1).txt')

# list2_Day1_2교재 20p~22p
# 1 << N : 원소가 n개일 경우, 모든 부분집합의 수
# i & (1<<j) : i의 j번째 비트가 1인지 아닌지 검사
# N :원소의 개수
# K : 부분집합원소의 합

# 3
# 3 6
# 5 15
# 5 10

T=int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    # print(N, K)

    arr = [i for i in range(1,13)]# 1부터 12를 원소로 가진 집합
    # print(arr)
    res = 0 # 조건 만족하는 부분집합 개수

    for i in range(1<<12): # 1<<N :부분 집합의 개수   # 모든 부분 집합 확인 
        sub_sum=0 # 부분집합 합
        sub=[]  #부분집합
        for j in range(12): # 원소의 수(12)만큼 비트를 비교함
            if i & (1<<j):   # i의 j번 비트가 1인 경우, 즉 j가 부분집합에 포함되는 경우,
                sub_sum += arr[j] # 포함되므로 합에 더해줌
                sub.append(arr[j]) # 부분집합리스트에도 추가

        if len(sub) == N and sub_sum== K:  #주어진 조건을 만족하는지 여부
            res += 1
    print(f'#{tc} {res}')   
   