T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split())
    boxes = [0] * (N+1)       # 버리는 0번 인덱스와 N개의 상자의 숫자를 담는 리스트 생성.
    for i in range(1, Q+1): # Q번 동안의 동작 동안
        l, r = map(int, input().split())
        for j in range(l, r+1):    # L번 상자부터 R번 상자까지의 숫자들을 i로 변경한다.
            boxes[j] = i
    print(f'#{tc}',*boxes[1:])