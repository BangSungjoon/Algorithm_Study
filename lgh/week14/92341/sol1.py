# 주차요금계산

import math

def solution(fees, records):
    answer = [] # 주차요금 담을 리스트
    dic = {} # key로 차번호, value로 입차시간 
    fee = {} # key로 차번호, value로 주차시간
    for i in records:
        arr = i.split() # ['23:00', '5961', 'OUT'] 
        # 입차한 경우
        if arr[2] == 'IN': 
            dic[arr[1]] = arr[0]  # 차량번호를 key, 입차시간을 value로 줌
        # 출차한 경우
        elif arr[2] == 'OUT':  
            H, M = map(int, arr[0].split(':')) # 출차시간을 시와 분으로 나눠줌
            h, m = map(int, dic[arr[1]].split(':')) # 입차시간을 시와 분으로 나눠줌
            M = (H * 60) + M # 출차시간 분으로 환산
            m = (h * 60) + m # 입차 시간 분으로 환산
            time = M - m # 총 주차 시간

            # 해당 차번호를 fee배열에 담아주기 (차번호가 key, 주차시간이 value) (출차한 차량 또 들어올 수 있음) fee에는 총 주차시간을 누적
            if arr[1] in fee: 
                fee[arr[1]] += time
            else:
                fee[arr[1]] = time

            del dic[arr[1]] # 출차 후 딕셔너리에서 제거  

    #차량이 출차하지 않는 경우
    if dic:
        for i in dic:
            h, m = map(int, dic[i].split(':')) # 입차시간
            H, M = 23, 59  # 출차시간 11시59분
            m = (h * 60) + m  
            M = (23 * 60) + 59 
            time = M - m
            if i in fee: 
                fee[i] += time
            else:
                fee[i] = time

    number = sorted(fee.keys())  # 차번호(key)들을 정렬한 리스트 number(오름차순)

    for i in number: # 차 번호 순으로 요금 계산
        time = fee[i]
        money = 0
        if time <= fees[0]: # 기본 시간보다 작거나 같으면 기본요금
            money = fees[1] 
        elif time > fees[0]: # 기본 시간보다 크면 (기본요금 +  추가 시간/단위 시간 * 단위요금 ) 
            money = (fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
        answer.append(money) 
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

