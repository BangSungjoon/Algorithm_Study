# 테스트 케이스 수
test = int(input())

for test_case in range(1, test+1) :
    # 2차원 배열 생성
    answer = 1
    sudoku = []
    for i in range(9) :
        sudoku.append(list(map(int, input().split())))
    
    # 가로 줄 확인
    for i in sudoku :
        if len(set(i)) != 9 :
            answer = 0
            break
    
    # 세로 줄 확인
    for i in range(0,9) :
        vertical_check = set()
        for j in range(0,9) :
            vertical_check.add(sudoku[j][i])
        if len(vertical_check) != 9 :
            answer = 0
            break
    
    # 3*3 확인
    for i in range(0,9,3) :
        for j in range(0, 9, 3) :
            cube_check = set()
            cube_check.add(sudoku[j][i])
            cube_check.add(sudoku[j+1][i])
            cube_check.add(sudoku[j+2][i])
            cube_check.add(sudoku[j][i+1])
            cube_check.add(sudoku[j+1][i+1])
            cube_check.add(sudoku[j+2][i+1])
            cube_check.add(sudoku[j][i+2])
            cube_check.add(sudoku[j+1][i+2])
            cube_check.add(sudoku[j+2][i+2])
            if len(cube_check) != 9 :
                answer = 0
                break
        break

    # 테스트 케이스 번호 출력 후 한 칸 띄고 정답 출력
    print(f'#{test_case} {answer}')