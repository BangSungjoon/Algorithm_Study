T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = [0] + list(map(int, input().split())) + [N]
    interval = [charger[i+1]-charger[i] for i in range(len(charger)-1)]

    """
    1. interval의 모든 요소가 K보다 작아야 함.
       즉, if interval에서 K보다 큰게 나오면 무조건 break
    """

    for i in range(M):
        if interval[i] > K:
            print(f'#{tc} 0')
            break
    else:
        cnt = 0
        for i in range(M-1):
            while len(interval) >= 2:
                if interval[i] + interval[i+1] <= K:
                    interval = interval[2:]
                    cnt += 1

                elif interval[i] + interval[i+1] > K:
                    interval = interval[1:]
                    cnt += 1

                if len(interval) == 2 and sum(interval) <= 3:
                    cnt -= 1

    print(f'#{tc} {cnt}')