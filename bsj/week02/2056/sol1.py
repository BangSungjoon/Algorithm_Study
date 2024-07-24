T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = str(input())
    days30 = ['04', '06', '09', '11']
    if int(N[4:6]) <= 0 or int(N[6:]) <= 0:
        print(f'#{test_case} -1')
    else:
        if N[4:6] in days30:
            if 30 < int(N[6:]) or int(N[6:]) < 1:
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {N[:4]}/{N[4:6]}/{N[6:]}')
        elif int(N[4:6]) == 2:
            if 28 < int(N[6:]) or int(N[6:]) < 1:
                print(f'#{test_case} -1')
            else:
                print(f'#{test_case} {N[:4]}/{N[4:6]}/{N[6:]}')
        else:
            print(f'#{test_case} {N[:4]}/{N[4:6]}/{N[6:]}')
