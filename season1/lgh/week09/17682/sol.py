def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isdigit():
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '#':
            score[-1] = score[-1] * (-1)
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] *2
    answer = sum(score)
    return answer