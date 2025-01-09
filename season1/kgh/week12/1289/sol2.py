import sys
sys.stdin = open('C:\\dev\\Algorithm_Study\\kgh\\week12\\1289\\input.txt')

T = int(input())
for tc in range(1, T+1):
    memory = input()
    N = len(memory)
    tmp = ['0'] * N
    cnt = 0
    
    while True:
        if tmp == list(memory):
            break
        for i in range(N):
            if tmp[i] != memory[i]:  # 현재 메모리 상태와 원래 메모리 상태가 다를 때
                # 해당 지점부터 끝까지 변경
                tmp[i:] = [memory[i]] * (N - i)
                cnt += 1  # 고친 횟수 증가
                break  # 변경 후 다음 단계로 넘어가기

    print(f"#{tc} {cnt}")