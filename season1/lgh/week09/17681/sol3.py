# 이진수 변환 함수
def func(num):
    binary_num = ''
    if num == 0:
        return 0
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2
    return binary_num


def solution(n, arr1, arr2):
    ans_arr = [[0]*n for _ in range(n)]  #arr1 변환한 최종 배열 담을 곳
    ans_arr2 = [[0]*n for _ in range(n)] #arr2 변환한 최종 배열 담을 곳
    #arr1을 받아와서 숫자 하나씩 이진수로 변환, 변환값을 r_ans에 담아줌
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
    
     #arr2을 받아와서 숫자 하나씩 이진수로 변환, 변환값을 r_ans에 담아줌
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
                if ans_arr[i][j] == 1: # 둘 다 1이면 벽#
                    ans_arr[i][j] = '#'
                else:                  # 아니면 공백''
                    ans_arr[i][j] = ' '    

            else:
                ans_arr[i][j] = '#'  # ans_arr[i][j]와 ans_arr2[i][j]가 다르면 #
                
    # result_arr=[]            
    # for row in ans_arr:              
    #     ans = ''.join(row)
    #     result_arr.append(ans)
    ans = [''.join(row) for row in ans_arr]
    return ans
    
   

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

#xf
