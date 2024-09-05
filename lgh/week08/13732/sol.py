import sys
sys.stdin=open('input.txt')
#시작좌표찾기
#끝좌표찾기
#시작과 끝좌표의 가로 세로 길이 확인, 내부가 채워져있는 지 확인

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    count = 0
    ans = 'no'
    # 시작좌표 찾기( 좌상단)
    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                start_x = i
                start_y = j
                flag = 1
                break  #for j 탈출
        if flag == 1:  #for i 탈출
            break
    #끝좌표 찾기
    flag = 0
    for i in range(N-1,-1, -1):   #끝좌표찾아야하므로 뒤에서부터 순회
        for j in range(N-1,-1,-1):
            if arr[i][j] == '#':
                end_x = i
                end_y = j
                flag=1
                break
        if flag == 1:
            break
    # 정사각형 확인하기(가로와 세로길이 같은 지, 시작좌표부터 끝좌표까지 다 #으로 채워졌는 지)
    if (end_x - start_x) == (end_y - start_y): #가로와 세로 길이 같은 지
        for i in range(start_x, end_y+1):  # 가로와 세로 길이 같다면 시작좌표부터 끝좌표까지 순회하며 #의 개수 세줌
            for j in range(start_y, end_y+1):
                if arr[i][j] == '#':
                    count += 1
        if count == (end_x - start_x) ** 2: #개수가 제곱수라면 정사각형
            ans = 'yes'

    print(f'#{tc} {ans}')

    #틀림 고쳐야함.....