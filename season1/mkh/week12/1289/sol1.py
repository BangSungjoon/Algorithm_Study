T = int(input())
for tc in range(1, T+1):
    init = list(input())
    ans = 0
    flag = '0'
    for char in init:
        if flag == '1':
            if char != flag:
                flag = '0'
                ans += 1
        else:
            if char != flag:
                flag = '1'
                ans += 1
    print(f'#{tc} {ans})
