# 백준 괄호
t = int(input())
ps = []
for _ in range(t):
    s = input()
    ps.append(s)

for i in range(t):
    string = ps[i]
    result = 0
    for s in string:
        if result < 0:
            break

        if s == "(":
            result += 1
        elif s == ")":
            result -= 1

    if result == 0:
        print('YES')
    else:
        print('NO')