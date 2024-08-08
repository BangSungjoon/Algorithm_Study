import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = [2, 3, 5, 7, 11]          # 나눠야 하는 소수를 인덱스로 만들기
    cnt = [0, 0, 0, 0, 0]           # 지수를 넣을 리스트 만들기
    for i in range(5):
        while N % num[i] == 0:
            cnt[i] += 1             # 나머지가 0이 될때까지 1씩 더해주기
            N //= num[i]            # 해당 소수로 값을 나누기
    print(f'#{tc} ', end = '')
    print(*cnt)                     # 리스트로 출력 안되게 바꾸어서 언패킹 후 출력