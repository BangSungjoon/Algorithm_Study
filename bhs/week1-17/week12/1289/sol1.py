T = int(input())

for tc in range(1, T+1):
    N = input()
    soodchacheck = '1'
    cnt = 0
    for i in N:
        if i == soodchacheck:
            cnt += 1
            if soodchacheck == '1':
                soodchacheck = '0'
            else:
                soodchacheck = '1'

    print(f'#{tc} {cnt}')
