import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    num_list= list(map(int, input()))
    # count = 0
    # max_num = 0
    # print(num_list)

    ##최댓값 찾기
    # for i in range(len(num_list)):
    #     if max_num < num_list[i]:  
    #        max_num = num_list[i]  
    #        if num_list[i] == max_num:
    #           count += 1
    # print(f'#{tc} {max_num} {count}')

    #최대빈도수와 빈도수 찾기
    count_list= [0] * 10    #0-9까지 count_list 리스트생성(카운트정렬)
    # print(count_list)
    for i in range(0, len(num_list)): 
        count_list[num_list[i]] += 1  
        max_count=0
        max_index=0
        for j in range(0, len(count_list)):
            if count_list[j]>= max_count:
                max_count= count_list[j]
                max_index = j

    print(f'#{tc} {max_index} {max_count}')
