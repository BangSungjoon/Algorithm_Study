# [백준] AC
t = int(input())

for _ in range(t):
    order = input()
    n = int(input())
    arr = input()

    if n == 0:
        # 입력받은 문자열의 길이가 0일 때
        q = []
    else:
        # 다루기 쉬운 list 형태로 변경
        q = arr[1:-1].split(',')

    reverse = False
    error = False

    for o in order:
        if o == 'R':
            reverse = not reverse
        elif o == 'D':
            if not q:
                error = True
                break
            if reverse:
                q.pop()
            else:
                q.pop(0)

    if error:
        print('error')
    else:
        if reverse:
            q.reverse()
        print('[' + ','.join(q) + ']')