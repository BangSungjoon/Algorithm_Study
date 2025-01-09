import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())  # 카드 장수
    cards = input()  # N개의 숫자 문자열로 입력 받음
    
    # 각 숫자의 출현 횟수를 저장할 딕셔너리
    count = {str(i): 0 for i in range(10)}
    
    # 각 숫자의 출현 횟수 계산
    for card in cards:
        count[card] += 1
    
    # 가장 많이 나타나는 숫자와 그 개수 찾기
    max_count = 0
    max_num = '0'
    
    for num, freq in count.items():
        if freq > max_count or (freq == max_count and int(num) > int(max_num)):
            max_count = freq
            max_num = num
    
    # 결과 출력
    print(f"#{tc} {max_num} {max_count}")