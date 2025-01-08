T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    max_rotate = N//4
    r_numbers = [''] * N
    s = input()
    for i in range(N):
        r_numbers[i] = s[i:i+max_rotate]
        if i+max_rotate > N:
            r_numbers[i] += s[0:i+max_rotate-N]
        r_numbers[i] = int(r_numbers[i],16)

    r_numbers = sorted(list(set(r_numbers)),reverse=True)

    print(f'#{tc} {r_numbers[K-1]}')