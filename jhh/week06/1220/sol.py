def attach_cnt(lst):
    result = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            if lst[j][i] == 1:  # N극 성질 자성체를 만나면
                cnt += 1
            elif lst[j][i] == 2:  # S극 성질 자성체를 만나면
                if cnt > 0:  # 이전에 N극 자성체가 존재했다면 교착 상태
                    result += 1
                    cnt = 0  # 교착 상태를 카운트했으니 다시 초기화
    return result

for _ in range(10):
    N = int(input())  # 정사각형 한 변의 길이 = 항상 100
    input_lst = [list(map(int, input().split())) for _ in range(100)]  # 100X100 행렬

    # 자성체 이동 처리
    for i in range(100):
        new_col = []
        for j in range(100):
            if input_lst[j][i] != 0:
                new_col.append(input_lst[j][i])

        new_col = [0] * (100 - len(new_col)) + new_col  # 남은 부분은 0으로 채움
        for j in range(100):
            input_lst[j][i] = new_col[j]

    # 교착 상태 개수 세기
    result = attach_cnt(input_lst)
    print(f"#{_ + 1} {result}")

