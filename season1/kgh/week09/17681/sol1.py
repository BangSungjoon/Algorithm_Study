def solution(n, arr1, arr2):
    # 각 비밀지도의 이진수 리스트
    map1 = [bin(a1)[2:].zfill(n) for a1 in arr1]
    map2 = [bin(a2)[2:].zfill(n) for a2 in arr2]

    # 결과를 담을 2차원 배열 (값 변경이 가능한 리스트 활용)
    result = [[''] * n for _ in range(n)]

    # 조건에 따라 결과 만들자
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':  # 둘 다 공백이면
                result[i][j] += ' '                      # 공백이다.
            elif map1[i][j] == '1' or map2[i][j] == '1': # 하나라도 벽이면
                result[i][j] += '#'                      # 벽이다.

    return [''.join(r) for r in result]                  # 결과 반환

# test_case_1
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))

# test_case_2
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
