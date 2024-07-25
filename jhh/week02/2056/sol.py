# 테스트 케이스 개수
T = int(input())

# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
thirty_one = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]

# 여러개의 테스트 케이스
for test_case in range(1, T + 1):
  date = input()

  # 입력값의 월이 1, 3, 5, 7, 8, 10, 12
  if int(date[4:6]) in thirty_one:
    if int(date[6:]) == 0 or int(date[6:]) > 31:
      print(f'#{test_case} -1')
    else:
      print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]}')

  # 입력값의 월이 4, 6, 9, 11
  elif int(date[4:6]) in thirty:
    if int(date[6:]) == 0 or int(date[6:]) > 30:
      print(f'#{test_case} -1')
    else:
      print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]}')

  # 입력값의 월이 2
  elif int(date[4:6]) == 2:
    if int(date[6:]) == 0 or int(date[6:]) > 28:
      print(f'#{test_case} -1')
    else:
      print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]}')

  # 입력값의 월이 1~12 사이 값이 아니면 -1 출력
  else:
    print(f'#{test_case} -1')