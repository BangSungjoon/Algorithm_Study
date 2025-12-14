T = int(input())

for t in range(T):
    command_list = input()

    top_l, top_r, bottom_l, bottom_r = [0, 0], [0, 0], [0, 0], [0, 0]

    turtle = [0, 0, 0]  # 0: 북, 1: 동, 2: 남, 3: 서
    for command in command_list:
        if command == 'F':
            if turtle[2] == 0:
                turtle[1] += 1
            if turtle[2] == 1:
                turtle[0] += 1
            if turtle[2] == 2:
                turtle[1] -= 1
            if turtle[2] == 3:
                turtle[0] -= 1
        elif command == 'B':
            if turtle[2] == 0:
                turtle[1] -= 1
            if turtle[2] == 1:
                turtle[0] -= 1
            if turtle[2] == 2:
                turtle[1] += 1
            if turtle[2] == 3:
                turtle[0] += 1
        elif command == 'L':
            turtle[2] = (turtle[2] - 1) % 4
        elif command == 'R':
            turtle[2] = (turtle[2] + 1) % 4

        # 1사분면
        if turtle[0] <= 0 and turtle[1] >= 0:
            if top_l[0] > turtle[0]:
                top_l[0] = turtle[0]
            if top_l[1] < turtle[1]:
                top_l[1] = turtle[1]
        # 2사분면
        if turtle[0] >= 0 and turtle[1] >= 0:
            if top_r[0] < turtle[0]:
                top_r[0] = turtle[0]
            if top_r[1] < turtle[1]:
                top_r[1] = turtle[1]
        # 3사분면
        if turtle[0] <= 0 and turtle[1] <= 0:
            if bottom_l[0] > turtle[0]:
                bottom_l[0] = turtle[0]
            if bottom_l[1] > turtle[1]:
                bottom_l[1] = turtle[1]
        # 4사분면
        if turtle[0] >= 0 and turtle[1] <= 0:
            if bottom_r[0] < turtle[0]:
                bottom_r[0] = turtle[0]
            if bottom_r[1] > turtle[1]:
                bottom_r[1] = turtle[1]

    width = abs(min(top_l[0], top_r[0], bottom_l[0], bottom_r[0]) - max(top_l[0], top_r[0], bottom_l[0], bottom_r[0]))
    length = abs(min(top_l[1], top_r[1], bottom_l[1], bottom_r[1]) - max(top_l[1], top_r[1], bottom_l[1], bottom_r[1]))

    print(width * length)

