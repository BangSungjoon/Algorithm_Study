T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split())
    boxes = [0] * N
    lrs = [[0,0] for _ in range(Q)]
    for i in range(Q):
        lrs[i] = map(int,input().split())
    lrs.reverse()
    for l, r in lrs:
        for i in range(l-1,r):
            if not boxes[i]: boxes[i] =Q
        Q -= 1
    print(f'#{tc}',*boxes)