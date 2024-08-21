import sys
sys.stdin = open('sample_input (4).txt')


T=int(input())
for tc in range(1,T+1):  
    N,Q=map(int,input().split())  # N개 상자, Q회동안 변경 
    # print(N,Q)
    lst = [0]*(N+1)   # 변경한거 넣을 리스트로, 1번 상자 부터 시작,,따라서 5번인덱스때문에 1개 더만듦
    for i in range(1,Q+1):   #1회면 리스트에 1, Q회면 리스트에 Q
        L,R=map(int,input().split())  # 변경할 범위인 L,R을 받아옴
        for j in range(L,R+1):  #범위인 L부터R까지 변경할 리스트순회하며
            lst[j]=i   #리스트에 몇회째인지 집어넣음

    print(f'#{tc}', *lst[1:])     














    # input_lst=[list(map(int,input().split())) for _ in range(Q)]
    # # print(input_lst)
    # for L,R in input_lst:
    #     for k in range(L,R+1):
    #         for j in range(1,len(input_lst)+1):
    #             lst[k]=j
    # print(lst)            