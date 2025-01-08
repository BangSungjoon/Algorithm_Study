import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = []
    for i in range(N):
        n1, n2 = map(int, input().split())
        num_lst.append([n1, n2])        # [[1, 3], [2, 5]]

    P = int(input())
    bus_stop = []
    for i in range(P):
        bus_stop.append(int(input()))       # [1, 2, 3, 4, 5]

    count_lst = []
    for num in bus_stop:
        count_num = 0
        for i in range(len(num_lst)):
            if num_lst[i][0] <= num <= num_lst[i][1]:
                count_num += 1
        count_lst.append(count_num)
    print(f'#{tc}', end=' ')
    print(*count_lst)



