T = int(input())

for testcase in range(1,T+1): # 큰 틀에서 1부터 T번 반복
    money=[50000, 10000, 5000, 1000, 500, 100, 50, 10]
    price = int(input()) #거스름돈입력받기
    print(f'#{testcase}') # #testcase 출력

    for i in money: 
        print(f'{price//i}', end=' ') #거스름돈 화폐단위 개수 출력(몫) ,end=' '통해 띄어쓰기가로정렬
        price %= i
    print() #밖의 for문 내용임..줄바꿈(각 테스트케이스 끝나고 줄바꿈)

#input.txt읽어오기까지 구현?

        
