import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i_lst = [list(input()) for _ in range(N)]   # 격자판 리스트
    visited = [[0] * N for _ in range(N)]   # 방문 기록 리스트
    rectangular = 0    # 정사각형 개수 count
    answer = True   # 하나의 정사각형이 되지 않을 시, answer를 false로

    # 완탐 고고
    for i in range(N):
        for j in range(N):

            # rectangular가 1 이상이고 방문하지 않은 곳인데 막혀있다면 하나의 정사각형이 되지 않기 때문에 false
            if not visited[i][j] and rectangular and i_lst[i][j] == '#':
                answer = False

            # 방문하지 않았고, 막혀있는 경우
            if not visited[i][j] and i_lst[i][j] == '#':
                check_r = 0 # 열 막혀있는 곳 count
                check_c = 0 # 행 막혀있는 곳 count

                # 열에 막혀있는 곳 세기
                while i < N and i_lst[i][j] == '#':
                   if i_lst[i][j] == '#':
                       check_c += 1
                       i += 1

                # 원래 i 위치로
                i -= check_c

                # 행에 막혀있는 곳 세기
                while j < N and i_lst[i][j] == '#':
                   if i_lst[i][j] == '#':
                       check_r += 1
                       j += 1

                # 원래 j 위치로
                j -= check_r

                cnt = 0
                # 열과 행에 막혀있는 곳의 개수가 같다면, 현재 위치부터 막혀있는 곳의 개수만큼 행, 열을 탐색해서 정사각형 범위에 막혀있는 곳 개수 세기
                if check_c == check_r:
                    for k in range(i, i+check_c):
                        for l in range(j, j+check_r):
                            # 막혀있는 곳을 count
                            if k < N and l < N and i_lst[k][l] == '#':
                                visited[k][l] = 1
                                cnt += 1

                    # 막혀있는 곳 개수가 정사각형의 크기와 같다면 정사각형 개수를 1 늘려주고, 아니라면 answer를 false로 바꾸기
                    if cnt == check_c*check_c:
                        rectangular += 1
                    else:
                        answer = False
                # 열과 행에 막혀있는 곳의 개수가 다르면, answer를 false로 바꾸기
                else:
                    answer = False

    # answer가 false이거나 정사각형 개수가 1이 아니라면 'no'를 출력
    if answer == False or rectangular != 1:
        print(f'#{tc} no')
    else:
        print(f'#{tc} yes')









