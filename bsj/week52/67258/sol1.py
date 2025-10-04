# 투포인터 알고리즘

def solution(gems):
    gems_num = len(set(gems))
    cart = {}   # 현재 구간 안의 보석 개수를 세는 dict
    types = 0   # 현재 구간 안에 들어있는 고유 보석 종류 수 
    left = 0    # 왼쪽 포인터
    result = (0, len(gems) - 1)   # 최적 구간
    
    for right in range(len(gems)):
        gem = gems[right]
        
        # 장바구니에 없는 종류의 보석이라면
        if gem not in cart:
            # 종류 추가하기
            cart[gem] = 0
            types += 1
        cart[gem] += 1  # 장바구니에 gem 개수 하나 증가

        # 현재 구간이 모든 보석 종류를 포함한다면
        while types == gems_num:
            # 지금 구간이 더 짧거나, 길이가 같다면 시작점이 더 작은 경우에 갱신 시키기
            if (right-left < result[1]-result[0]) or (right-left == result[1]-result[0] and left < result[0]):
                result = (left, right)
            
            # 왼쪽 보석을 하나 빼면서 구간 줄여보기
            left_gem = gems[left]
            cart[left_gem] -= 1
            left += 1
            if cart[left_gem] == 0:
                del cart[left_gem]
                types -= 1
            
    return [result[0]+1, result[1]+1]