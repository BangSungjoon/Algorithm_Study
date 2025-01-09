import sys
sys.stdin = open('input.txt', 'r')

# test_case 개수 input
T = int(input())
for test_case in range(1, T+1):
    N = input() # N input
    k = 1 # 배수 계산 위한 k 정의
    num_list = [] # 자릿수 리스트

    while len(num_list) < 10: # 0~9까지 모두 추가될 때까지 반복
        current_N = int(N) * k # 현재 N = n * k로 정의
        k += 1 # k는 1씩 증가
        for n in str(current_N): # 현재 N의 자릿수를
            if n not in num_list: # 자릿수 리스트에 없다면
                num_list.append(n) # 추가한다.
    print(f'#{test_case} {current_N}') # 결과 출력