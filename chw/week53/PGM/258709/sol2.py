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
    max_win = 0
    result = []

    for A_choice in dice_comb:
        # B의 선택
        B_choice = []
        for j in range(len(dice)):
            if j not in A_choice:
                B_choice.append(j)

        B_choice = tuple(B_choice)  # 키 값으로 쓰려면 튜플로 변환

        A_sums = sorted(dice_dict[A_choice].copy())
        B_sums = sorted(dice_dict[B_choice].copy())

        # print('a', A_sums)
        # print('b', B_sums)

        # A와 B 대결 결과 A가 승리한 횟수 비교
        win = 0

        for a in A_sums:
            max_idx = 1e9

            start = 0
            end = len(B_sums) - 1

            while start <= end:
                mid = (start + end) // 2

                if a > B_sums[mid]:     # 이긴 경우
                    max_idx = mid
                    start = mid + 1
                else:                   # 지거나 비긴 경우
                    end = mid - 1

            if max_idx == 1e9:
                pass                    # 하나도 못 이긴 경우 pass
            else:
                win += (max_idx + 1)    # idx에 1 더해주면 이긴 갯수

        if max_win < win:
            max_win = win
            result = A_choice

    # 결과 출력
    result = list(result)
    for r in range(len(result)):
        result[r] += 1                  # 주사위 인덱스라 번호로 변경

    return result