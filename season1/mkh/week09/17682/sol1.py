def solution(dartResult):
    darts = [0]*3
    bonuses = ['D', 'S', 'T']
    s = ''
    index = 0
    for c in dartResult:
        if c.isdigit():
            s+=c
        elif c in bonuses:
            darts[index] = int(s) ** (bonuses.index(c)+1)
            s = ''
            index += 1
        else:
            if c == '#':
                darts[index-1] *= -1
            else:
                darts[index-1] *= 2
                darts[index-2] *= 2

    return sum(darts)
