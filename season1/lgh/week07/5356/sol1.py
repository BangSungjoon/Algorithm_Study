T=int(input())
for tc in range(1,T+1):
    lst=[list(input() )for _ in range(5)]  #5행짜리 배열
    res=''
    maxlen=0
    for word in lst: #5행짜리 배열에서 한 행씩 뽑아 제일 긴 행을 뽑음
        if len(word) > maxlen:
            maxlen=len(word)  #제일 긴 행 뽑음

    for j in range(maxlen):
        for i in range(5):
            if j < len(lst[i]):  #다음 열로 넘어가기전까지만 더함
                res+=lst[i][j]

    print(f'#{tc} {res}')