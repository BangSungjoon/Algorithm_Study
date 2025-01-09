import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line_list = [list(map(int, input().split())) for _ in range(N)] # [A, B]로 이루어진 리스트

    P = int(input())
    cnt_list = [0] * P
    for j in range(P):
        C = int(input())
        cnt = 0 
        for line in line_list:
            if line[0] <= C <= line[1]:  # 노선에 포함되면
                cnt += 1  # 카운트 횟수 증가
        cnt_list[j] = cnt

    print(f'#{tc}', *cnt_list)
