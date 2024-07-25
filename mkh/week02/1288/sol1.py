T = int(input())

for tc in range(1,T+1):
    sheep = int(input())
    n_sheep = 0
    ori_sheep = sheep

    counter = {}
    for i in range(10):
        counter[str(i)] = 0
    num= 0
    while 0 in list(counter.values()):
        str_sheep = str(sheep)
        for cha in str_sheep:
            counter[cha] += 1
        num += 1
        sheep += ori_sheep
    print(f'#{tc} {num*ori_sheep}')