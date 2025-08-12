from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))

comb = permutations(num_list, 2)

good = set()

for c in comb:
    num = c[0] + c[1]

    if num in num_list:
        good.add(num)

print(len(good))