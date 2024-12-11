# 시간 초과

import sys
import itertools
from itertools import product
sys.stdin = open('input.txt')

list = [0,1,2,3,4,5,6,7,8,9,10]
num = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
data = itertools.product(list, repeat=num)
result_info = []
for i in data:
    # print(i)
    number = [0] * 11
    for j in range(num):
        number[i[j]] += 1
    peach_score = 0
    lion_score = 0
    for k in range(10):
        if not info[k] and not number[k]:
            continue
        elif info[k] >= number[k]:
            peach_score += 10-list[k]
        else:
            lion_score += 10-list[k]
    if lion_score > peach_score:
        result_info.append((lion_score-peach_score, number))

result_info.sort(key=lambda x:x[0], reverse=True)
if result_info:
    print(result_info[0][1])
else:
    print([-1])


