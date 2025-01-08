import sys
sys.stdin = open('input.txt')

# arr = [1, 2, 3]
# subsets = [[]]
#
# for num in arr:
#   size = len(subsets)
#   for y in range(size):
#     subsets.append(subsets[y]+[num])
# print(subsets)      # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
subsets = [[]]
for num in A:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y] + [num])

T = int(input())

for tc in range(1, T+1):
    # n: 개수, k: 합
    n, k = map(int, input().split())
    count_num = 0

    for arr in subsets:
        if len(arr) == n and sum(arr) == k:
            count_num += 1
    print(f'#{tc} {count_num}')