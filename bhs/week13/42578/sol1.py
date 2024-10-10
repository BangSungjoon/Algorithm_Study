def solution(clothes):
    # 의상 종류별로 개수를 세기 위한 딕셔너리
    clothes_dict = {}
    
    # 의상 종류별로 개수 세기
    for name, category in clothes:
        if category in clothes_dict:
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1
    
    # 조합 계산
    result = 1
    for count in clothes_dict.values():
        # 각 종류별로 (안 입는 경우 + 해당 종류의 옷 수)를 곱함
        result *= (count + 1)
    
    # 아무것도 입지 않는 경우 제외
    return result - 1
