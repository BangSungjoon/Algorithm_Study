from collections import defaultdict


def solution(fees, records):
    dic = defaultdict(list)
    for record in records:
        time, num, _ = record.split()
        dic[num].append(int(time[:2]) * 60 + int(time[3:]))
    # 시간, 차번호를 받아서 defaultdict에 이력한다. 값들은 0:00 기준 분으로 치환해서 입력한다.
    for key in dic:
        if len(dic[key]) % 2:
            dic[key].append(1439)
            # 만약 출입차 기록이 홀수일 경우, 출차가 안찍힌 것이므로 23:59에 출차했다고 기록을 입력해준다.
        temp = [0] * (len(dic[key]) // 2)
        for i in range(0, len(dic[key]), 2):
            temp[i // 2] = dic[key][i + 1] - dic[key][i]
            # 앞뒤 기록의 차이를 주차요금 시간으로 담아서 temp에 입력한다.
        dic[key] = sum(temp)
            # 총 주차시간의 합을 값으로 집어넣는다.
    # defaultdict(<class 'list'>, {'5961': 146, '0000': 334, '0148': 670})
    keys = sorted(dic.keys())
    answer = [0] * len(keys)
    for i in range(len(keys)):
        if dic[keys[i]] <= fees[0]:
            answer[i] = fees[1]
            # 기본 시간 이하라면 기본 요금만
        elif (dic[keys[i]] - fees[0]) % fees[2]:
            answer[i] = fees[1] + ((dic[keys[i]] - fees[0]) // fees[2] + 1) * fees[3]\
            # 기본 시간을 초과했고, 단위 시간에 딱 맞추지 않아서 올림해야 할 경우
        else:
            answer[i] = fees[1] + ((dic[keys[i]] - fees[0]) // fees[2]) * fees[3]
            # 기본 시간을 초과했고, 단위 시간에 딱 맞았을 경우

    return answer


