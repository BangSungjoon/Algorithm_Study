# 12712번 [파리 잡기 3] D2

SW Expert `12712` `파리 잡기 3` 난이도 : D2

```python
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    fly_arr = []

    for i in range(N):
        fly_arr.append(list(map(int, input().split())))

    plus_shape = 0
    x_shape = 0
    Max_sum = 0

    for i in range(N):
        for j in range(N):
            plus_shape = fly_arr[i][j]
            x_shape = fly_arr[i][j]
            for k in range(1, M):
                if j-k >= 0:
                    plus_shape += fly_arr[i][j-k]
                if j+k < N:
                    plus_shape += fly_arr[i][j+k]
                if i-k >= 0:
                    plus_shape += fly_arr[i-k][j]
                if i+k < N:
                    plus_shape += fly_arr[i+k][j]

                if i-k >= 0 and j-k >= 0:
                    x_shape += fly_arr[i-k][j-k]
                if i+k < N and j+k < N:
                    x_shape += fly_arr[i+k][j+k]
                if i-k >= 0 and j+k < N:
                    x_shape += fly_arr[i-k][j+k]
                if i+k < N and j-k >= 0:
                    x_shape += fly_arr[i+k][j-k]

                if Max_sum < plus_shape:
                    Max_sum = plus_shape
                if Max_sum < x_shape:
                    Max_sum = x_shape
    print(f'#{test_case} {Max_sum}')
```

+방향으로 잡거나, x방향으로 잡을 때 많이 잡는 경우를 구하는 문제

### 난관 1.

2차원 배열을 입력 받는 법을 몰라 공부해야 했다.
원소에 리스트를 추가하는 방식으로 해결했다.

```python
arr = []

for i in range(B):    
	arr.append(list(map(int, input().split())))
```

### 난관 2.

범위를 벗어난 경우 값을 포함 시키지 않을 방법을 찾아야 했다.
범위를 벗어난 모든 경우 마다 if문을 추가하여 해결했다. 더 깔끔한 방법이 있으면 고쳐보고 싶다.

```python
if j-k >= 0:
	plus_shape += fly_arr[i][j-k]
if j+k < N:
	plus_shape += fly_arr[i][j+k]
if i-k >= 0:
	plus_shape += fly_arr[i-k][j]
if i+k < N:
	plus_shape += fly_arr[i+k][j]

if i-k >= 0 and j-k >= 0:
	x_shape += fly_arr[i-k][j-k]
if i+k < N and j+k < N:
  x_shape += fly_arr[i+k][j+k]
if i-k >= 0 and j+k < N:
	x_shape += fly_arr[i-k][j+k]
if i+k < N and j-k >= 0:
	x_shape += fly_arr[i+k][j-k]
```