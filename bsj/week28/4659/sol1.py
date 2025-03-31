moum = 'aeiou'

while True:
    password = input()
    if password == 'end':
        break

    has_moum = any(c in moum for c in password)
    if not has_moum:
        print(f'<{password}> is not acceptable.')
        continue

    is_acceptable = True
    moum_cnt = 0
    zaum_cnt = 0

    for i in range(len(password)):
        if password[i] in moum:
            moum_cnt += 1
            zaum_cnt = 0
        else:
            zaum_cnt += 1
            moum_cnt = 0

        if moum_cnt == 3 or zaum_cnt == 3:
            is_acceptable = False
            break

        if i < len(password) - 1:
            if password[i] == password[i+1] and password[i] not in ['e', 'o']:
                is_acceptable = False
                break

    if is_acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')