def solution(friends, gifts):
    
    name_table = {}
    for i, friend in enumerate(friends):    # key-value(이름-숫자) 
        name_table[friend] = i
        
    # num_gifts[i][j]: i가 j에게 준 선물의 개수
    num_gifts = [[0] * len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        giver, receiver = gift.split()
        num_gifts[name_table[giver]][name_table[receiver]] += 1
    
    # gifts_index: 선물 지수 
    gifts_index = [0] * len(friends)
    
    transposed_num_gifts = list(zip(*num_gifts))
    
    for friend in friends:
        i = name_table[friend]
        gifts_index[i] = sum(num_gifts[i]) - sum(transposed_num_gifts[i])
    
    #최대 선물 저장할 변수 
    max_gifts = 0
    
    for i, receiver in enumerate(friends):
        gifts = 0
        for j, giver in enumerate(friends):
            if i == j:
                continue
            
            if num_gifts[i][j] > num_gifts[j][i]:
                gifts += 1
            elif num_gifts[i][j] == num_gifts[j][i]:
                if gifts_index[i] > gifts_index[j]:
                    gifts += 1
        max_gifts = max(max_gifts, gifts)
    

    return max_gifts