def solution(coin, cards):
    n = len(cards)
    target = n + 1

    my_cards = set(cards[:n // 3])  # 처음 뽑은 카드
    keep_cards = set()  # 라운드마다 뽑는 카드

    # 처음 뽑은 카드에서 가능한 쌍 있는지 미리 계산
    pre_set = 0
    temp_my_cards = list(my_cards)
    for card in temp_my_cards:
        if target - card in my_cards:
            pre_set += 1
            my_cards.discard(card)
            my_cards.discard(target - card)

    turn = 0

    # 카드 뭉치에 남은 카드가 없을 때까지 진행
    for i in range(n // 3, n, 2):
        turn += 1
        # print(turn, '턴')
        # print('i', i)

        # 카드 드로우
        keep_cards.add(cards[i])
        keep_cards.add(cards[i + 1])

        # print('카드 상황', my_cards)
        # print('킵 카드', keep_cards)

        # 게임 진행
        is_success = False
        # 1. 원래 있는 카드 내에서 2개 내기
        if pre_set:
            pre_set -= 1
            is_success = True
            # print('1번 성공')

        # 2. 1번이 실패했다면 뽑은 카드 1개랑 매칭되는지
        if not is_success:
            for my_card in my_cards:
                if target - my_card in keep_cards and coin >= 1:
                    my_cards.remove(my_card)
                    keep_cards.remove(target - my_card)
                    coin -= 1
                    is_success = True
                    # print('2번 성공')
                    break

        # 3. 2번도 실패했다면 뽑은 카드 2개로 되는지
        if not is_success:
            for keep_card in keep_cards:
                if target - keep_card in keep_cards and coin >= 2:
                    keep_cards.remove(keep_card)
                    keep_cards.remove(target - keep_card)
                    coin -= 2
                    is_success = True
                    # print('3번 성공')
                    break

        # 다음 라운드 진행 여부
        if not is_success:
            # print('끝')
            break
        elif i + 2 > n - 1:  # 카드 뭉치가 끝난 경우
            turn += 1
            # print('끝')
            break
    return turn