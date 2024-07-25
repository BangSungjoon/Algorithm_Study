# 2056 연월일 달력
import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스
T = int(input())

for t in range(1, T+1) :
    date = str(input())

    answer = -1

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    
    if int(month) in months_31 :
        if 0 < int(day) <= 31 :
            answer = f'{year}/{month}/{day}'
    elif int(month) in months_30 :
        if 0 < int(day) <= 30 :
            answer = f'{year}/{month}/{day}'
    elif int(month) == 2 :
        if 0 < int(day) <= 28 :
            answer = f'{year}/{month}/{day}'
    
    print(f'#{t} {answer}')