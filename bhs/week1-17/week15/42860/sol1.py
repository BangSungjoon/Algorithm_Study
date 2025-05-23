def solution(name):
    if set(name) == {'A'}:    # 두번 꺾는 경우는 고려하지 않음
        return 0
    
    a_pos = ord('A') # 'A' : 65, 'Z' : 90
    z_pos = ord('Z')
    
    answer = float('inf')
    
    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] #왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i: :-1] + name[i+1:][::-1] # 기준점에서 빠꾸 + 좌측
        for n in [l_r,r_l]:
            while n and n[-1] == 'A': # 끝에 A들은 셀 필요 없으므로 자르기
                n = n[:-1]
            cnt = [min(ord(c)-a_pos, (z_pos+1) - ord(c)) for c in n ]
            answer = min(answer, i + (len(cnt)-1) + sum(cnt))

    return answer
