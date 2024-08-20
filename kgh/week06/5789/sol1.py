import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0 for _ in range(1, N+1)]  # N개의 0으로 이루어진 box 리스트
    for i in range(1, Q+1):  # i는 1, 2, ... Q
        L, R = map(int, input().split())
        for n in range(L-1, R):  # 인덱스 말고, 실제 L번째 박스부터 R번ㅉ 박스까지
            boxes[n] = i  # i로 채우기
    print(f'#{tc}', *boxes)
