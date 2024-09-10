def solution(n, arr1, arr2):
    # 각 비밀지도의 이진수 리스트
    map1 = [bin(a1)[2:].zfill(n) for a1 in arr1]
    map2 = [bin(a2)[2:].zfill(n) for a2 in arr2]

    # 한줄에 우겨넣기 (시간은이 이중for문보다 적게 드는 듯)
    return [''.join('#' if (r1 == '1' or r2 == '1') else ' ' for r1, r2 in zip(row1, row2)) for row1, row2 in zip(map1, map2)]

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
