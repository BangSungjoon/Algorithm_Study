def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    n_str1 = [str1[i] + str1[i+1] for i in range(len(str1)-1) if (str1[i] + str1[i+1]).isalpha()]
    n_str2 = [str2[i] + str2[i+1] for i in range(len(str2)-1) if (str2[i] + str2[i+1]).isalpha()]
    # 두글자씩 뗀 애들을 n_str1, n_str2로 저장

    if not (n_str1 or n_str2):          # 둘 중 하나라도 비어 있다면
        if not (n_str1 and n_str2):     # 둘 다 비어있다면 1, 하나만 비어있으면 0
            return 65536
        else: return 0
    inters = set(chars for chars in n_str1 if chars in n_str2)      # 교집합의 세트 몇 개인지 구하기
    inter_amount = 0                                                # 교집합이 총 몇번 등장하는지 구하기
    for inter in inters:
        inter_amount += min(n_str1.count(inter), n_str2.count(inter))

    return int(inter_amount/(len(n_str1)+len(n_str2)-inter_amount)*65536)