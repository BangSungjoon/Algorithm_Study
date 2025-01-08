import sys
sys.stdin = open('input.txt', 'r')

# 테스트케이스 개수
T = int(input())
for test_case in range(1, T + 1):
    date = input() # 테스트케이스 한줄 input
    year = date[:4] # 년 추출
    month = date[4:6] # 월 추출
    day = date[-2:] # 일 추출
    
    # -1을 반환할 경우 분기
    if month == '02' and (int(day)>28 or int(day)<1): # 제일 특이한 2월 먼저 분기
        print(f"#{test_case} -1")
    elif month in ['04', '06', '09', '11'] and (int(day)>30 or int(day)<1): # 30일까지인 달 분기
        print(f"#{test_case} -1")
    elif month in ['01', '03', '05', '07', '08', '10', '12'] and (int(day)>31 or int(day)<1): # 31일까지인 달 분기
        print(f"#{test_case} -1")
    elif month == '00': # 00인 경우,,?
        print(f"#{test_case} -1")
    else: # 그 외에 모두 정상!
        print(f"#{test_case} {'/'.join([year, month, day])}")
   