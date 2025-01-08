def solution(dartResult):
    # 제곱값 딕셔너리
    square = {'S': 1, 'D': 2, 'T': 3}
    score = []
    tmp = ''  # 두자리수 담기 위한 tmp
    for i, dart in enumerate(dartResult):
        if dart.isdigit():    # 두자리수일 경우 (10일 경우) 처리
            tmp += dart
        elif dart.isalpha():  # 영역별 제곱 처리
            score.append(int(tmp) ** square[dart])
            tmp = ''          # tmp 초기화
        elif dart == '*':     # 옵션 * 처리
            if len(score) == 1:  # 점수가 하나인 경우
                score[-1] = score[-1] * 2  # 맨 마지막 숫자만 2배
            elif len(score) >= 2:  # 점수가 두개 이상인 경우
                score[-2:] = [s*2 for s in score[-2:]]  # 이번, 저번 점수 2배
        elif dart == '#':     # 옵션 # 처리      
            score[-1] = -score[-1]  # 이번 점수 마이너스 처리
    return sum(score)  # 다 더한 값 출력


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))