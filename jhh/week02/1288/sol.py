# 테스트 케이스 개수
T = int(input())

set_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 여러개의 테스트 케이스
for test_case in range(1, T + 1):
  N = int(input())
  new_list = []
  i =  0
  while True:
    i += 1

    # N을 문자열로 리스트에 넣기
    new_list += list(str(N*i))

    # 모든 숫자를 다 봤을 때, 마지막에 본 숫자 출력 -> 애매한 문장으로 인해 오래 걸림
    if set(new_list) == set(set_list):
      print(f'#{test_case} {N*i}')
      break