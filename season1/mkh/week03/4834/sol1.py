T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cards = list(map(int,input()))
    frequency = [0]*10 # 카운트 정렬 할 빈 리스트 생성
    for card in cards:
        frequency[card] += 1 # 카드의 등장회수를 frequency list에 할당
    max_num = 0
    max_frequency = 0
    for i in range(10):
        if max_frequency<=frequency[i]: #i의 등장횟수가 제일 클 경우, num과 빈도수에 리턴. 작은 수부터 큰 수의 순서로 탐색하므로 큰 수가 우선으로 등록됨.
            max_frequency = frequency[i] 
            max_num = i
    print(f'#{tc} {max_num} {max_frequency}')