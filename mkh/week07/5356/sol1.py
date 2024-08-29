T = int(input())

for tc in range(1, T+1):
    ls = [list(input()) for _ in range(5)]  # 5줄 받아오기 str으로 받아왔으므로 index 접근이 가능함.
    
    nls = [['']*5 for _ in range(15)]       # 행렬 전환해서 받아올 new_list 받아오기

    for i in range(5):
        for j in range(len(ls[i])):
            nls[j][i] = ls[i][j]            # 행렬 전환

    print(f'#{tc}',end=' ')
    for lis in nls:
        for item in lis:
            print(item, end='')             # 각 줄의 아이템들을 띄어쓰기 없이 프린트한다.
    print()