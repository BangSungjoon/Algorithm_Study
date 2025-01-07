def solution(fees, records):
    parkings = []
    answer = []
    
    for i in range(len(records)):
        if records[i][-2:] == "IN":     # 입차 기록일 경우
            for j in range(i, len(records)):
                # 출차 기록이 있는 지 검사
                if records[j][6:] == records[i][6:11]+'OUT':
                    # 출차 기록이 있다면
                    hour = int(records[j][:2]) - int(records[i][:2])
                    minute = int(records[j][3:5]) - int(records[i][3:5])
                    break
            else:
                # 출차 기록이 없다면 23:59에 나갔다.
                hour = 23 - int(records[i][:2])
                minute = 59 - int(records[i][3:5])
            time = 60 * hour + minute
            # parking의 구조 [차량번호, 이용시간]
            for parking in parkings:
                # 이미 이용한 기록이 있다면 시간 추가
                if parking[0] == int(records[i][6:10]):
                    parking[1] += time
                    break
            else:
                parkings.append([int(records[i][6:10]), time])

    sorted_parkings = sorted(parkings, key=lambda x: x[0])
    
    for sorted_parking in sorted_parkings:
        if fees[0] >= sorted_parking[1]:
            answer.append(fees[1])
        else:
            time = sorted_parking[1] - fees[0]
            fee = fees[1]
            # 몫이 나누어떨어질 때만 추가 요금을 부과하고, 그렇지 않으면 올림 처리
            fee += ((time + fees[2] - 1) // fees[2]) * fees[3]
            answer.append(fee)
    
    return answer
