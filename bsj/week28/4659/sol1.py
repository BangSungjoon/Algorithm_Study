# 비밀번호 발음하기
password = input()
moum = 'aeiou'
result = 'acceptable.'
while password != 'end':
    moum_cnt = 0
    zaum_cnt = 0
    break_point = False

    for i in range(5):
        if moum[i] in password:
            break
    else:
        print(f'<{password}> is not acceptable.')
        password = input()
        continue

    for i in range(len(password)):
        if password[i] in moum:
            if zaum_cnt > 0:
                zaum_cnt = 0
            moum_cnt += 1
        else:
            if moum_cnt > 0:
                moum_cnt = 0
            zaum_cnt += 1
        if moum_cnt == 3 or zaum_cnt == 3:
            print(f'<{password}> is not acceptable.')
            password = input()
            break_point = True
            break
    if break_point:
        continue
    if i < len(password)-1 and password[i] != 'e' and password[i] != 'o':
        if password[i] == password[i+1]:
            print(f'<{password}> is not acceptable.')
            password = input()
            continue

    print(f'<{password}> is acceptable.')
    password = input()