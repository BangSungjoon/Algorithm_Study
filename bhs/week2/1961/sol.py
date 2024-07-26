def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_180(matrix):
    return [list(reversed(row)) for row in reversed(matrix)]

def rotate_270(matrix):
    return list(reversed(list(zip(*matrix))))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotate_90(matrix)
    rot_180 = rotate_180(matrix)
    rot_270 = rotate_270(matrix)

    print(f'#{t}')
    for i in range(N):
        print(''.join(map(str, rot_90[i])), ''.join(map(str, rot_180[i])), ''.join(map(str, rot_270[i])))