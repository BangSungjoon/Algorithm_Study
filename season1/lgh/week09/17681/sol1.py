def func(num):
    binary_num = ''
    if num == 0:
        return 0
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2
    return binary_num


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    ans_arr = [[0]*n for _ in range(n)]
    ans_arr2 = [[0]*n for _ in range(n)]
    #arr1을 받아와서 숫자 하나씩 이진수로 변환, 변환값을 r_ans에 담아줌(뒤에 공백있어서 한번 더 순회돌았음)
    for j in range(len(arr1)):  
        ans = func(arr1[j])
        r_ans = ''
        for s in ans:
            r_ans += s
        # n보다 작으면 앞에 0으로 채워줌       
        if len(r_ans) < n:
            r_ans = '0'*(n-len(r_ans)) + r_ans
            #ans_arr에 담아줌
        ans_arr[j] = list(map(int,r_ans))
    
     #arr2을 받아와서 숫자 하나씩 이진수로 변환, 변환값을 r_ans에 담아줌(뒤에 공백있어서 한번 더 순회돌았음)
    for j in range(len(arr2)):  
        ans = func(arr2[j])
        r_ans = ''
        for s in ans:
            r_ans += s
        # n보다 작으면 앞에 0으로 채워줌       
        if len(r_ans) < n:
            r_ans = '0'*(n-len(r_ans)) + r_ans
            #ans_arr에 담아줌
        ans_arr2[j] = list(map(int,r_ans))


    #ans_arr와 ans_arr2를 비교함
    for i in range(n):
        for j in range(n):
            if ans_arr[i][j] == ans_arr2[i][j]:
                if ans_arr[i][j] == 1:
                    ans_arr[i][j] = '#'
                else:
                    ans_arr[i][j] = ' '    

            else:
                ans_arr[i][j] = '#'

    for row in ans_arr:              
        ans = ''.join(row)
        print(f'#{tc} {ans}')

