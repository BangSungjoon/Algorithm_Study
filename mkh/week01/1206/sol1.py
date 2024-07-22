import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, 11):
    total_sum = 0
    result = 0
    size = int(input())
    env = list(map(int,input().split()))
    for t in range(2,size-2):
        if env[t] >= max([env[t-2],env[t-1],env[t],env[t+1],env[t+2]]):
            total_sum += env[t] - max([env[t-2],env[t-1],env[t+1],env[t+2]])
    print(f'#{tc} {total_sum}')