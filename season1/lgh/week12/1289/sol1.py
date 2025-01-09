# 원석이의 메모리 복구
# 모든 비트 0에서 원래상태로 만드는 데 최소 수정
# startmemory는 모든 비트가 0
# memory는 원래 비트

import sys 
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1,T+1):
    memory = list(map(int,input())) # 원래 메모리
    startmemory = [0] * len(memory) # 모든비트0인 메모리
     
    count = 0
    for i in range(len(memory)):
        if startmemory[i] != memory[i]:
            count += 1
            for j in range(i,len(startmemory)):
                startmemory[j] = memory[i]
       

    print(f'#{tc} {count}')

