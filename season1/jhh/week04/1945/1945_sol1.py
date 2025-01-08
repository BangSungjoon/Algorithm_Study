import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    def seperate(N, a):
        count_num = 0
        while N % a == 0:
            count_num += 1
            N = N // a
        return count_num
 
    under_lst = [2, 3, 5, 7, 11]
    
    print(f'#{tc}', end=' ')
    for num in under_lst:
        print(seperate(N, num), end=' ')
    print()



