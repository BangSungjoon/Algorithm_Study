from itertools import combinations, product


def solution(dice):
    dice_comb = list(combinations(range(len(dice)), len(dice) // 2))

    dice_dict = {}

    # 주사위를 선택했을 때 나올 수 있는 모든 합의 경우의 수를 저장
    for dice_set in dice_comb:
        # print(dice_set)

        dice_nums = []

        for i in list(dice_set):
            dice_nums.append(dice[i])

        dice_sum = [sum(prod) for prod in product(*dice_nums)]
        dice_dict[dice_set] = dice_sum

    # 대결
    max_cnt = 0
    result = []

    for A_choice in dice_comb:
        # B의 선택
        B_choice = []
        for j in range(len(dice)):
            if j not in A_choice:
                B_choice.append(j)

        B_choice = tuple(B_choice)  # 키 값으로 쓰려면 튜플로 변환

        # A와 B 대결 결과 A가 승리한 횟수 비교
        cnt = 0
        for a in dice_dict[A_choice]:
            for b in dice_dict[B_choice]:
                if a > b:
                    cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            result = list(A_choice)

    for r in range(len(result)):
        result[r] += 1

    return result