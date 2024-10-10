#42578 의상
def solution(clothes):
    answer = 1

    ootd = {}   # ootd 딕셔너리 생성(의상종류를 key로)
    for name, type in clothes:
        if type in ootd:
            ootd[type].append(name)
        else:
            ootd[type] = [name]

    for type in ootd:   # value+1을 딕셔너리 끝까지 곱함
        answer *= len(ootd[type])+1  # +1은 안입는 경우 더해줌

    return answer - 1  # 최소 한 개는 착용해야 하므로 -1