# [1차] 다트 게임
def solution(dartResult):
    result = []     # 게임 결과를 저장해둘 빈 리스트

    for i in range(len(dartResult)-1):  # 10의 경우 i+1을 해야하므로 범위를 하나 줄여준다.
        if dartResult[i].isdigit():     # 숫자라면
            if dartResult[i] == '1' and dartResult[i+1] == '0': # 너 혹시 10이니?
                score = 10              # ㅇㅇ 10임 ㅋ
                idx = i+2               # 보너스 index는 2칸 뒤부터
            else:                           # 님 10 아님?
                score = int(dartResult[i])  # 정수로 바꿔
                idx = i+1                   # 보너스 index는 1칸 뒤부터
            while idx < len(dartResult):    # 자 범위 넘어가면 끝나는 겁니다?
                if dartResult[idx].isdigit():
                    break                   # 물론 다음 숫자 나와도 끝남
                elif dartResult[idx] == 'D':
                    score **= 2
                elif dartResult[idx] == 'T':
                    score **= 3
                elif dartResult[idx] == '*':
                    score *= 2
                    if len(result) > 0:     # 혹시 이전 숫자 있습니까?
                        result[-1] *= 2     # 두배 늘리세요
                elif dartResult[idx] == '#':
                    score = -score
                idx += 1                    # 보너스 index 하나 증가
            result.append(score)            # 결과에 저장 시켜
    answer = sum(result)                    # 합체 시켜

    return answer