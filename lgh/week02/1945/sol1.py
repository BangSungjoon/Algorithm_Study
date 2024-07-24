import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    N=int(input())
    dict={2:0, 3:0, 5:0, 7:0, 11:0}
    print(f"#{test_case}", end=' ') 
 
    for key in dict: #key는 key만 출력(value출력X)  #for key in x.keys():로 써도 key만 출력
        while True:  # while에 True를 지정하면 무한 루프
            if N % key == 0:
                dict[key]+=1 
                N=N//key  #몫 할당
            else:
                break
        
        print(dict[key], end=' ')    
    print() #for in 문 한번 돌고 개행  