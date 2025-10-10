from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    # 조합
    itertools_combinations = list(combinations(list(range(len(dice))), len(dice) // 2))
    answer = []
    total_dice = set(range(len(dice)))
    max_sum = -1
    for com in itertools_combinations:
        sum_result = 0
        
        a_dice = []
        for c in com:
            a_dice.append(dice[c])
        b_dice = []
        b_com = total_dice - set(com)  # 차집합으로 b의 주사위를 구하기
        for c in b_com:
            b_dice.append(dice[c])
        # a의 합을 구해보자
        a_product = list(map(sum, product(*a_dice)))
        # b의 합
        b_product = list(map(sum, product(*b_dice)))
        b_product.sort()
        
        for a in a_product:
            sum_result += bisect_left(b_product, a)
        if sum_result > max_sum:
            max_sum = sum_result
            answer = com
    
    return [i+1 for i in answer]