import sys
sys.stdin = open('C:\\dev\\Algorithm_Study\\kgh\\week12\\1289\\input.txt')

T = int(input()) 

for tc in range(1, T + 1):
    memory = input() 
    cnt = 0  # 변경 횟수
    current = '0'  # 초기 메모리 상태 -> 모두 '0'으로 이루어짐
    
    # 메모리의 각 비트 순회
    for i in range(len(memory)):
        if memory[i] != current:  # 현재 비트가 이전 상태와 다를 경우
            cnt += 1  # 변경 횟수를 증가
            current = memory[i]  # 현재 상태를 업데이트
    
    print(f"#{tc} {cnt}")