from itertools import product


def solution(users, emoticons):
    discount_rate = [40, 30, 20, 10]

    total_emoticon_plus = 0
    total_profit = 0

    # 할인율 순열
    discount_rate_product = list(product(discount_rate, repeat=len(emoticons)))

    # 할인된 이모티콘으로 완전탐색
    for rates in discount_rate_product:
        emoticon_list = [[emoticons[i], rates[i]] for i in range(len(rates))]
        emoticon_plus = 0
        profit = 0

        # 유저 한 명씩 이모티콘 플러스와 구매 총액 계산
        for user in users:
            user_rate = user[0]
            user_budget = user[1]

            purchased = 0

            for price, rate in emoticon_list:
                # 유저의 할인율보다 크면 구매
                if rate >= user_rate:
                    purchased += price * (100 - rate) / 100

                # 예산 넘어가면 이모티콘 플러스로 전환
                if purchased >= user_budget:
                    emoticon_plus += 1
                    break
            # 이모티콘 플러스로 전환 안 됐으면 이모티콘 수익 기록
            else:
                profit += purchased

        # 이모티콘 플러스와 수익 정산
        if emoticon_plus > total_emoticon_plus:
            total_emoticon_plus = emoticon_plus
            total_profit = profit
        elif emoticon_plus == total_emoticon_plus:
            total_profit = max(total_profit, profit)

    ans = [total_emoticon_plus, total_profit]

    return ans