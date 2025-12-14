N = int(input())
signal = input()
line = N // 5

arr = [['.'] * line for _ in range(5)]
arr[0][0] = signal[0]

for i in range(1, len(signal)):
    arr[i // line][i % line] = signal[i]


num_list = [['#####', '#...#', '#####'],['#####'],['#.###', '#.#.#', '###.#'],['#.#.#', '#.#.#', '#####'],
            ['###..', '..#..', '#####'],['###.#', '#.#.#', '#.###'],['#####', '#.#.#', '#.###'],
            ['#....', '#....', '#####'],['#####', '#.#.#', '#####'],['###.#', '#.#.#', '#####']]

def check_num(k):
    res = []

    for j in range(3):
        if k+j >= line:
            break

        l = ''
        for i in range(5):
            l += arr[i][k+j]

        res.append(l)

    # 숫자 반환
    for idx, num in enumerate(num_list):
        if res == num:
            return idx
    else:
        return 1

x = 0
res = ''

while x < line:
    if arr[0][x] == '.':
        x += 1
    elif arr[0][x] == '#':
        num = check_num(x)

        if num != 1:
            res += str(num)
            x += 4
        elif num == 1:
            res += str(num)
            x += 2

print(res)