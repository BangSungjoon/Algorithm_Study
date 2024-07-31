T = int(input())

for test_case in range(1, T+1):
  N = int(input())
  input_lst = list(map(int, input()))

  # 주어진 리스트에서 최대값 찾기
  max_num = input_lst[0]
  for num in input_lst:
    if num > max_num:
      max_num = num

  # count 리스트에, 주어진 리스트의 최대값 수만큼 "0" 만들기
  count_lst = [0] * (max_num+1)

  # 각 숫자(인덱스화)가 몇 개인지 count
  for i in range(N):
    count_lst[input_lst[i]] += 1      # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
  # print(count_lst)

  index_num = 0
  count_max = count_lst[0]
  for i in range(max_num+1):
    if count_lst[i] >= count_max:
      index_num = i
      count_max = count_lst[i]

  print(f'#{test_case} {index_num} {count_max}')