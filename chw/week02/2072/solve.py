import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    sum_odd = 0
    row = list(map(int, input().split()))
    for num in row:
        if num % 2 == 1:
            sum_odd = sum_odd + num
    print(f'#{t+1} {sum_odd}')












# line1 = int_num[1:11]
# line2 = int_num[11:21]
# line3 = int_num[21:]

# def add_odd(numbers, *args):
#     result = 0
#     for i in args:
#         if i%0 != 0:
#             result = result + i
#         else:
#             pass
#         return result

# print(add_odd(line1))

