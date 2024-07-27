# 1961 숫자 배열 회전

import sys
sys.stdin = open("input.txt", "r")

# 90도 회전하게 만드는 함수
def rotate_matrix(arr, arr_size) :
    
    # 회전한 배열을 저장할 리스트 생성
    arr_rotated = [[0 for row in range(arr_size)] for col in range(arr_size)]

    for x in range(arr_size) :
        for y in range(arr_size) :
            # 회전시 index의 상관관계
            # 이전 y 값이 이후 x 값으로 들어가고
            # 이전 x값 + 이후 y 값 = arr 인덱스 제일 마지막 번호(배열 크기에서 1만큼 뺀 것)
            arr_rotated[y][arr_size-1-x] = arr[x][y]
    
    return arr_rotated
    

# 테스트 케이스 입력
T = int(input())

for t in range(1, T+1) :
    N = int(input())

    arr = []

    for i in range(N) :
        arr.append(list(map(int, input().split())))
    
    arr_90 = rotate_matrix(arr, N)
    arr_180 = rotate_matrix(arr_90, N)
    arr_270 = rotate_matrix(arr_180, N)
    
    # 답 출력
    print(f'#{t}')
    for i in range(N) :
        row_90 = ''.join(list(map(str, arr_90[i])))
        row_180 = ''.join(list(map(str, arr_180[i])))
        row_270 = ''.join(list(map(str, arr_270[i])))
        print(row_90, row_180, row_270)
    