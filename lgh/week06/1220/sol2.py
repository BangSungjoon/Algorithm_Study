import sys
sys.stdin=open('input.txt')   
# 1은 빨강 2는 파랑

for tc in range(1,11): 
    N=int(input())
    arr=[list(map(int, input().split()))for _ in range(N)]
    count=0  #교착상태 카운트할 변수
    for i in range(len(arr)):
        condition=False  #열이 바뀔때마다 condition 초기화
        for j in range(len(arr)):    
            if arr[j][i]==1:   #빨강색이면  condition을 True로
                condition=True  
            elif arr[j][i]==2: #파란색이면 condition이 True인 경우, count해줌( 즉 이전에 빨강색을 만났어야했음)
                if condition:
                    count+=1 
                condition=False   #파란색을 만나면 다시 condition을 초기화해줌
                 
    print(f'#{tc} {count}')
    