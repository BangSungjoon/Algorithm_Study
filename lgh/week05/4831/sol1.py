import sys 
sys.stdin=open('sample_input (1).txt')


T= int(input())
for tc in range(1,T+1):
    K, N, M =map(int, input().split())
    M_arr=[0]+list(map(int, input().split()))+[N]
    # print(K, N, M)
    # print(M_arr)
    start=0
    res=0

    for i in range(1,M+2): #도착지 N포함이므로 도착지N의 인덱스(M+1)까지
        if M_arr[i] - M_arr[i-1] > K:  
            res = 0
            break
        if M_arr[i] - start > K:
            start = M_arr[i-1]
            res += 1

    print(f'#{tc}', res)        

