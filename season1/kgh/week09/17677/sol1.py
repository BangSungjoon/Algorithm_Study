def solution(str1, str2):
    N, M = len(str1), len(str2)
    # 두글자로 이루어진 부분집합 리스트 생성
    ss1 = [str1[i:i+2].lower() for i in range(N-1) if str1[i:i+2].isalpha()]
    ss2 = [str2[i:i+2].lower() for i in range(M-1) if str2[i:i+2].isalpha()]

    # 나중을 위한 복사본 생성
    copy_ss2 = ss2.copy()
    len_intersection = 0  # 공집합 길이 구하기 위한 변수
    for s in ss1:  # ss1을 순회하면서
        if s in copy_ss2:  # ss2에 있다면
            copy_ss2.remove(s)  # ss2에서 지우고
            len_intersection += 1  # 교집합 길이에 + 1

    # 합집합 길이 = 집합1의 길이 + 집합2의 길이 - 교집합의 길이
    len_union = len(ss1) + len(ss2) - len_intersection

    # 자카드 유사도 계산. 단, 둘 다 0이라면 1로 계산하여 65536 반환
    return int(len_intersection / len_union * 65536) if (len_intersection != 0 or len_union != 0) else 65536

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
