def solution(dartResult):
    n = ''   #숫자만을 담을 문자열
    score = []  #계산된 값을 담을 리스트
    for i in dartResult: 
        if i.isdigit(): # 숫자면 n에 담아줌 
            n += i
        elif i == 'S':   # 'S'면   1제곱해주고 계산된값을 score리스트에 담음, 숫자문자열 n을 비워줌
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
            if len(score) > 1:   # score 길이가 1개보다 많으면 뒤에서 2개 꺼내오고 1개면 뒤에서 1개만 꺼내옴 
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] *2
    answer = sum(score) #score리스트에 담긴 값 더해줌
    return answer