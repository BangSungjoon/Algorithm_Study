def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    best_goal = [0, 0]
    
    def dfs(idx, current_sale):
        if idx == len(emoticons):
            subscribers, revenue = simulate(users, emoticons, current_sale)
            # 목표 1 : subscribers 최대화, 목표 2 : revenue 최대화
            if subscribers > best_goal[0] or (subscribers == best_goal[0] and revenue > best_goal[1]):
                best_goal[0] = subscribers
                best_goal[1] = revenue
            return
        # 가능한 모든 할인율을 시도
        for s in sale:
            dfs(idx + 1, current_sale + [s])
    dfs(0, [])
    return best_goal


def simulate(users, emoticons, sale):
    subscribers = 0
    revenue = 0
    
    for rate, threshold in users:
        total = 0
        for i in range(len(emoticons)):
            if sale[i] >= rate: # 기준 할인율보다 큰 할인을 하는 이모티콘만 구매
                total += emoticons[i] * (100 - sale[i])/100
        if total >= threshold:
            subscribers += 1
        else : 
            revenue += total
    return subscribers, int(revenue)
