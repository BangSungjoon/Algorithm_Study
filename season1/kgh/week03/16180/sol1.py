import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 수만큼 순회
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 숫자 길이.. 굳이 사용해야 할까
    cards = input() # 숫자카드 입력받기
    cards_cnt = {} # 카드 별 개수 저장할 빈 딕셔너리 생성
    for card in cards:
        if card in cards_cnt: # 딕셔너리에 이미 있으면 1 더해줌
            cards_cnt[card] += 1
        else:
            cards_cnt[card] = 1 # 딕셔너리에 없으면 1로 새로 할당

    max_num = max(cards_cnt, key = lambda x: (cards_cnt[x], x)) # 카운트가 가장 많은 카드
    max_num_cnt = cards_cnt[max_num] # 카운트가 가장 많은 카드의 카운트 수
    
    # 결과 출력
    print(f'#{test_case} {max_num} {max_num_cnt}')