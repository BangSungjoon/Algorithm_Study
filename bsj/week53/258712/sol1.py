def solution(friends, gifts):
    answer = {}
    present = {} # 선물 지수
    chart = {} # 준사람/받은사람 표
    for f in friends:
        present[f] = 0
        chart[f] = {}
        for r in friends:
            if r != f:
                chart[f][r] = 0
        answer[f] = 0
    
    # 선물지수와 표 구하기
    for g in gifts:
        준사람, 받은사람 = g.split()
        present[준사람] += 1
        present[받은사람] -= 1
        chart[준사람][받은사람] += 1
        
    # 누가 선물 받을지 정하기
    visited = set()
    for f in friends:
        visited.add(f)
        for r in friends:
            if r not in visited:
                if chart[f][r] > chart[r][f]:
                    answer[f] += 1
                elif chart[r][f] > chart[f][r]:
                    answer[r] += 1
                else:
                    if present[f] > present[r]:
                        answer[f] += 1
                    elif present[r] > present[f]:
                        answer[r] += 1

    result = 0
    for f in friends:
        result = max(result, answer[f])
    return result