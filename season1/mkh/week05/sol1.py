T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    charger = [0] + list(map(int,input().split())) +[N]
    dists = [0]*(M+1)
    for i in range(M+1):
        dists[i] = charger[i+1]-charger[i] # 충전기 간의 거리 리스트
    
    impo = False
    for dist in dists:
        if dist > K: # 충전기 간의 거리가 주행 가능 거리보다 멀면 0을 출력하고, impossible = True로 입력.
            print(f'#{tc} 0')
            impo = True
            break
    if impo:
        continue
    
    charges = 0
    temp = 0

    for i in range(M+1):
        if temp + dists[i]>K:
            temp = dists[i]
            charges += 1
        else: temp += dists[i]
    print(f'#{tc} {charges}')