import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    price = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
     
    print(f'#{test_case}')
    
    arr = []
    for m in money:
        arr.append(price//m)
        price %= m
    print(*arr)