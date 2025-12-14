T = int(input())

for t in range(T):
    command_list = input()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    direction = 0   # 0: 북, 1: 동, 2: 남, 3: 서

    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for command in command_list:
        if command == 'F':
            x += dx[direction]
            y += dy[direction]
        elif command == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif command == 'L':
            direction = (direction-1) % 4
        elif command == 'R':
            direction = (direction+1) % 4

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    width = abs(min_x - max_x)
    length = abs(min_y - max_y)

    print(width * length)