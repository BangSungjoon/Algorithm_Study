def solution(n, arr1, arr2):
    for i in range(n):
        n1 = bin(arr1[i])[2:]
        n2 = bin(arr2[i])[2:]
        if len(n1) < n:
            n1 = '0'*(n - len(n1)) + n1
        if len(n2) < n:
            n2 = '0' * (n - len(n2)) + n2
        arr1[i] = n1
        arr2[i] = n2
    # 빈 배열 만들기
    answer = [[' ']*n for _ in range(n)]
    # or 연산으로 채워넣기
    for i in range(n):
        for j in range(n):
            if int(arr1[i][j]) | int(arr2[i][j]):
                answer[i][j] = '#'
        answer[i] = ''.join(answer[i])

    return answer