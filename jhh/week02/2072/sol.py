# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):
  # 테스트 케이스를 문자열 리스트로 받기
  test_list = input().split()
  new_list = []

  for i in range(10):
    # 문자를 정수로 변환하고 홀수 확인 후, 리스트에 추가
    if int(test_list[i]) % 2 == 1:
      new_list.append(int(test_list[i]))

  # 합 출력
  print(f'#{test_case} {sum(new_list)}')