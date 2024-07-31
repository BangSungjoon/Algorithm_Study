T = int(input())
for tc in range (1, T+1):
    s, K = input().split()
    K = int(K)
    s_poss = [0.0] *3
    for i in range(3):
        if s[i] == 'o':
            s_poss[i] = 1.0
    # 컵이 있는 곳을 1로 치환.

    for i in range(K): # K번 동안 섞기를 반복. 사이드에 있을 경우 무조건 가운데로, 가운데에서는 절반의 확률로 양쪽으로 간다.
        s_poss[0], s_poss[1], s_poss[2] = s_poss[1]/2, s_poss[0]+s_poss[2], s_poss[1]/2
    
    poss_max = 0

    for i in range(2,-1,-1): # 같은 확률일 경우 왼쪽의 인덱스를 반환해야 하므로 거꾸로 카운트한다.
        if poss_max<=s_poss[i]:
            poss_max = s_poss[i]
            poss_index = i

    print(f'#{tc} {poss_index}')