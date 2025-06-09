# 길이가 M인, N개의 자연수 중 M개를 고른 수열

from itertools import permutations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

ans = permutations(num_list, M)

# 사전 순으로 증가하는 순서로 출력
for a in sorted(ans):
    print(*a)