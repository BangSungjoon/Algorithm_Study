T = int(input())

for tc in range(1, T+1):
  N = int(input())
  c_velocity = 0
  c_distance = 0
  
  for i in range(N):
    input_s = input()

    # 입력값이 0일 경우
    if input_s == "0":
      # 현재 속도 = 이전 속도
      # 누적 거리 = 이전 거리 + 이전 속도(=현재 속도)
      c_distance += c_velocity

    else:
      state, arr = map(int, input_s.split())
      
      # 가속
      if state == 1:
        c_velocity += arr
        c_distance += c_velocity
      
      # 감속
      if state == 2:
        if c_velocity < arr:
          c_velocity = 0
        else:
          c_velocity -= arr
          c_distance += c_velocity

  print(f'#{tc} {c_distance}')