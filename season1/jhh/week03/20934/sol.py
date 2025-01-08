T = int(input())

for tc in range(1, T+1):
  bubble, k = map(str, input().split())
  k = int(k)

  # 처음에 첫 번째 컵에 있을 경우
  if bubble[0] == 'o':
    if k % 2 == 0:
      print_num = 0
    else:
      print_num = 1

  # 처음에 두 번째 컵에 있을 경우    
  elif bubble[1] == 'o':
    if k % 2 == 0:
      print_num = 1
    else:
      print_num = 0

  # 처음에 세 번째 컵에 있을 경우
  else:
    if k == 0:
      print_num = 2
    elif k % 2 == 0:
      print_num = 0
    else:
      print_num = 1
      
  print(f'#{tc} {print_num}')