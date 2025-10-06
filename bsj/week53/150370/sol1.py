# [프로그래머스] 개인정보 수집 유효기간
from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    today_year, today_mon, today_day = map(int, today.split('.'))
    today_total = today_day + today_mon*28 + today_year*12*28
    terms_dict = defaultdict(int)
    for term in terms:
        name, month = term.split()
        terms_dict[name] = int(month)
    
    for i in range(len(privacies)):
        join_day, rule = privacies[i].split()
        join_year, join_mon, join_day = map(int, join_day.split('.'))
        join_total = join_day + join_mon*28 + join_year*12*28 + terms_dict[rule]*28
        if today_total >= join_total:
            answer.append(i+1)
        
    return answer