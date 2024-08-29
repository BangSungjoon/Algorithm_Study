import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N : 화덕의 크기, # M : 피자 개수
    N, M = map(int, input().split())
    # 치즈의 양
    cheese = list(map(int, input().split()))
    # [순서, 치즈의 양]으로 구성된 리스트
    pizza_cheese = [[i+1, cheese[i]] for i in range(M)]
    oven = pizza_cheese[:N]  # 오븐에 첫판 굽자!
    remain_pizza = pizza_cheese[N:]  # 남은 피자들

    while len(oven) > 1:  # 오븐에 1개의 피자가 남을 때까지 반복
        if oven[0][1] != 0:  # 1번위치 피자의 치즈가 0이 아니면
            re_oven = oven.pop(0)  # 오븐에 다시 넣기 위해 pop해서 임시변수에 저장
            oven.append([re_oven[0], re_oven[1]//2])  # 오븐의 맨 뒤에 [순서, 치즈의 양] 추가

        elif oven[0][1] == 0:  # 1번 위치 피자의 치즈가 0일 때
            oven.pop(0)  # 다 녹았으니까, 뺌
            if remain_pizza:  # 구워야 할 피자가 있으면
                add_pizza = remain_pizza.pop(0)  # 오븐에 넣기 위해 pop해서 임시변수에 저장
                oven.append([add_pizza[0], add_pizza[1]//2]) # 오븐의 맨 뒤에 [순서, 치즈의 양] 추가

    print(f'#{tc} {oven[0][0]}')