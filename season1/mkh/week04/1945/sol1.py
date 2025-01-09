T = int(input())
num_ls = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    ls = [0]*5 # 카운트용 리스트 할당
    N = int(input())
    for i in range(5):
        while N % num_ls[i] == 0: # 소인수분해할 수 있을 때까지
            N /= num_ls[i] # 나누고
            ls[i] += 1 #카운트를 더해준다
    print(f'#{tc}', *ls)
