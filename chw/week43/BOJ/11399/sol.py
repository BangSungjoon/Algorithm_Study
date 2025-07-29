import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
time.sort()

waiting_time = [0] * N
waiting_time[0] = time[0]

for t in range(1, N):
    waiting_time[t] = waiting_time[t-1] + time[t]

print(sum(waiting_time))