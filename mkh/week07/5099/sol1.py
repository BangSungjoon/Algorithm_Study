T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())             # N = 화덕의 크기, M = 총 피자의 갯수
    bake = [0] * N                              # 화덕을 위한 빈 리스트 할당
    bake_i = [0] * N                            # 화덕에 들어간 피자의 인덱스를 위한 빈 리스트 할당
    cnt = -N                                    # 다 구워진 피자의 갯수를 세기 위한 변수 할당. 처음에 피자가 들어갈 때 다 구운 것처럼 체크하므로 -N을 초기 값으로 설정.
    cheezes = list(map(int,input().split()))    # 치즈 수들의 리스트 받기.
    front = 0                                   # 피자가 들어가는 위치를 체크하기 위한 front
    while cnt < M-1:                            # 마지막 한 피자만 남을 때까지
        for i in range(N):                      # 화덕에 들어갈 수 있는 피자들을 모두 체크하는데
            if bake[i] == None:                 # 넣을 수 있는 피자도 없고, 안에 있는 피자도 구워졌다면 패스
                continue
            elif bake[i]//2 == 0 and front <= M-1:  # 피자가 다 구워졌는데 아직 구울 피자가 남아있다면
                bake[i] = cheezes[front]            # 화덕에 피자를 새로 넣고
                bake_i[i] = front                   # 피자의 인덱스를 bake_i에 갱신한다.
                cnt += 1                            # 다 구워진 피자의 개수를 +1 하고
                front += 1                          # 다음에 들어갈 피자의 인덱스를 +1 해준다.
            elif bake[i]//2 == 0:                   # 피자가 다 구워졌는데 추가로 구울 피자가 없다면
                bake[i] = None                      # 화덕에 None 값을 할당하고
                cnt += 1                            # 다 구워진 피자의 개수에 +1 한다.
            else: bake[i] //= 2                     # 다 구워지지 않았다면, 피자의 양을 절반으로 한다.

            if cnt == M-1:                          # 피자가 하나만 남았다면, 화덕을 순회하는 것을 중단한다.
                break
    for i in range(N):
        if bake[i] != None:                         # 화덕에 남은 피자 i에 대해
            print(f'#{tc} {bake_i[i]+1}')           # i에 들어간 인덱스를 확인한 후 +1하여 출력한다.