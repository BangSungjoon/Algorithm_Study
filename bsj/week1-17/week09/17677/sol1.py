def solution(str1, str2):
    new_str1 = []   # 알파벳만 대문자로 바꿔서 넣을 리스트 두개
    new_str2 = []
    for i in range(len(str1)-1):    # i번째와 그 다음이 알파벳이라면
        if str1[i].isalpha() and str1[i+1].isalpha():
            new_str1.append(str1[i].upper()+str1[i+1].upper())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            new_str2.append(str2[i].upper() + str2[i+1].upper())

    # 만약 둘다 공집합일 경우
    if not new_str1 and not new_str2:
        answer = 65536
        return answer

    # 교집합의 개수
    test1 = set(new_str1)   # in을 사용할 때 hash table을 사용해서
    test2 = set(new_str2)   # 빨리 찾기 위함 + 중복 없애기
    x_cnt = 0   # 교집합 개수
    s_cnt = 0   # 합집합 개수
    for s in test1:         # 교집합은 두 집합에 다 있는 원소 일 때
        if s in test2:      # 가장 적은 개수이다.
            x_cnt += min(new_str1.count(s), new_str2.count(s))
            s_cnt += max(new_str1.count(s), new_str2.count(s))  # 합집합은 두 집합이 겹친다면 더 개수가 많은 것으로
        else:               # 두 집합이 겹치지 않는다면 있는 쪽의 개수만큼 추가
            s_cnt += new_str1.count(s)
    for s in test2:         # 합집합 = 차집합1 + 차집합2 + 교집합
        if s not in test1:
            s_cnt += new_str2.count(s)
    # 자카드 유사도 계산
    answer = int((x_cnt / s_cnt)*65536)

    return answer