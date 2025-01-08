def solution(n, arr1, arr2):
    n_arr1 = []
    n_arr2 = []
    for num in arr1:
        s = ''
        for i in range(n):
            s = str(num % 2) +s
            num //= 2
        n_arr1.append(s)

    for num in arr2:
        s = ''
        for i in range(n):
            s = str(num % 2) + s
            num //= 2
        n_arr2.append(s)

    answer = []
    for i in range(n):
        s = ''
        for j in range(n):
            if n_arr1[i][j] == '1' or n_arr2[i][j] == '1':
                s += '#'
            else: s += ' '
        answer.append(s)
    return answer