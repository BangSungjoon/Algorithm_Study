from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    n_str1 = [str1[i] + str1[i+1] for i in range(len(str1)-1) if (str1[i] + str1[i+1]).isalpha()]
    n_str2 = [str2[i] + str2[i+1] for i in range(len(str2)-1) if (str2[i] + str2[i+1]).isalpha()]
    # 두글자씩 뗀 애들을 n_str1, n_str2로 저장

    # 둘 다 공집합이면, 65536 리턴
    if not (n_str1 and n_str2):
        return 65536

    c1 = Counter(n_str1)
    c2 = Counter(n_str2)

    inter = sum((c1&c2).values())
    union = sum((c1|c2).values())

    return int(inter/union * 65536)