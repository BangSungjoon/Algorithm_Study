#### 내가 쓴 식이 아닌데~~~~~ 나도 라이브러리 좀 써보고 싶다~~~~~~~~~


from collections import Counter
from functools import reduce

def solution(clothes):
    # 의상 종류별로 개수를 세기
    clothes_counter = Counter([kind for name, kind in clothes])
    
    # 각 종류별 선택 방법의 수 계산 (해당 종류 선택 안 함 + 선택 가능한 옷의 수)
    choices = [count + 1 for count in clothes_counter.values()]
    
    # 모든 선택 방법을 곱하고 1을 빼기 (아무것도 선택하지 않는 경우 제외)
    total_combinations = reduce(lambda x, y: x * y, choices) - 1
    
    return total_combinations
