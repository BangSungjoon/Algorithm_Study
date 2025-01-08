T = int(input())

b = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
  money = int(input())
  a = []
  for change in b:
    if money >= change:
      a.append(money//change)
      money = money%change
    else:
      a.append(0)
  print(f'#{test_case}')
  print(*a)