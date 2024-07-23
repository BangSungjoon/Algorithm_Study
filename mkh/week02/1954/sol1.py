T = int(input())
for tc in range(1,T+1):
    size = int(input())
    snail = []
    wall = 0
    hor = 0
    ver = 0
    dir = 0 #0이면 오른쪽, 1이면 아래쪽, 2면 왼쪽, 3이면 위쪽
    checker = 0
    for i in range(size):
        snail.append([])
        for j in range(size):
            snail[i].append(j)

    for i in range(size**2):
        snail[ver][hor]=i+1
        checker +=1
        if checker+wall == size:
            checker = 0
            if dir%4==0:
                wall +=1
            elif dir%4==2:
                wall +=1
            dir +=1

        if dir%4 == 0:
            hor +=1
        elif dir%4 ==1:
            ver +=1
        elif dir%4 ==2:
            hor -=1
        else:
            ver -=1
    
    print(f"#{tc}")
    for i in range(size):
        for j in range(size):
            print(snail[i][j],end=" ")
        print()