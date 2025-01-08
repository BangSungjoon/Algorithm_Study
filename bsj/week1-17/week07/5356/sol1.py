# 의석이의 세로로 말해요
T = int(input())
 
for test_case in range(1, T + 1):
    word_list = ['']*5  # input을 받아올 리스트
    cnt = 0             # result의 인덱스
    n = 0               # 정답 문자열의 길이(총 글자수)
    max_len = 0         # 단어별 길이 중 최대 값
 
    for i in range(5):  # 단어 리스트 만들기, 단어별 길이 측정
        word_list[i] = input()
        n += len(word_list[i])              # 들어온 단어 만큼 총 글자수 증가
        if max_len < len(word_list[i]):     # 최대 단어 길이 구하기
            max_len = len(word_list[i])
 
    result = ['']*n     # 정답 리스트
 
    for j in range(max_len):    # 각 단어당 최대 길이까지 순회
        for i in range(5):
            if j < len(word_list[i]):
                result[cnt] = word_list[i][j]
                cnt += 1
 
    # 결과를 문자열로 결합
    result_str = ''.join(result)
 
    # 결과 출력
    print(f'#{test_case} {result_str}')