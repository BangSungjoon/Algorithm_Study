import sys 
sys.stdin=open('sample_input (1).txt')


T= int(input())
for tc in range(1,T+1):
    K, N, M =map(int, input().split())
    M_arr=[0]+list(map(int, input().split()))+[N] #시작점과 도착지를 충전소리스트에 더함
    # print(K, N, M)
    # print(M_arr)
    start=0
    res=0

    for i in range(1,M+2): #도착지 N포함이므로 도착지N의 인덱스(M+1)까지
        if M_arr[i] - M_arr[i-1] > K:   # 바로 다음 충전소까지의 간격이 K보다 크면 0, for문 탈출
            res = 0
            break
        if M_arr[i] - start > K: #0부터 정류장까지의 거리가 k보다 커질떄 start를 바로 직전정류장으로 갱신한뒤, 충전 횟수늘림
            start = M_arr[i-1]
            res += 1

    print(f'#{tc}', res)     

