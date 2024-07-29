# 16180 숫자 카드

import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스
T = int(input())

for t in range(1, T+1) :
    # 카드 장수
    N = int(input())

    # 카드 숫자를 담을 list
    cards = [int(i) for i in input()]

    # 가장 많은 카드 장수를 저장할 dict
    # card -> 카드 숫자, num_of_card -> 그 숫자 카드의 장수
    max_card =  {
        'card' : cards[0] ,
        'num_of_card' : cards.count(cards[0])
    }

    for card in cards :
        # 현재 순회 중인 카드의 장수가 저장되어있는 카드 장수보다 많을 경우
        if cards.count(card) > max_card.get('num_of_card') :
            # 갱신
            max_card['card'] = card
            max_card['num_of_card'] = cards.count(card)
        # 장수가 서로 같을 경우 & 카드가 더 클 경우
        elif cards.count(card) == max_card.get('num_of_card') and card > max_card.get('card'):
            # 갱신
            max_card['card'] = card
            max_card['num_of_card'] = cards.count(card)
    
    print(f'#{t} {max_card.get("card")} {max_card.get("num_of_card")}')
    
