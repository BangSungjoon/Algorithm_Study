# 1979 어디에 단어가 들어갈 수 있을까

## 2차원 배열 생성
## `list_name.append(list(map(int, input().split())))` 

### `input()`
사용자가 입력이 가능하도록, 사용자가 입력한 내용은 문자열(string)으로 return 됨
### `input().split()`
1. `input()` 으로 받은 string을 공백 기준으로 분할 → list로 return
2. (EX) 사용자 입력 → "1 2 3" , return → ['1', '2', '3']   
### `map(int, input().split())`
1.  `map` 함수 → 첫 번째 인자로 주어진 함수를 두 번째 인자의 모든 요소에 적용시킴
    - return 된 list의 각 요소에 `int` 함수 적용
2. (EX) `map(int, ['1', '2', '3'])` → `[1, 2, 3]`
### `list(map(int, input().split()))`
1.  `map`의 함수 결과를 list로 변환
### `list_name.appened(...)`
1. 최종적으로 얻은 list를 기존 리스트(list_name)에 추가
2. (EX) 처음에 list_name 빈 리스트 []라면,

    list_name.append([1, 2, 3])를 실행한 후 → list_name : [[1, 2, 3]]

## sol 1
### 처음 접근
가로 / 세로 따로 한칸씩 비교해보면서 K의 흰색칸이 이어지는지 확인

→ 너무 고려해야할 조건이 많아짐
### 문제 풀이
step 1 . 가로 / 세로 한 줄을(list) string 형태로 변환
step 2 . 0을 기준으로 `.split()`
step 3 . `.split()`으로 인해 생성된 list를 for문 돌리기
step 4 . list 안 요소의 길이가 K와 같은지 판별 → 같다면 `answer += 1`

## sol 2
### 접근 방법
string 말고 list를 그대로 사용해보자 !

### `if puzzle[i][j] == 0 or j == N-1` 
K만큼 긴 단어가 들어갈 수 있는 자리인지, 혹은 그보다 큰지/작은지를 구분할 if 문의 조건을 작성하는 것이 어려웠다. 

cnt가 K랑 정확히! 맞는다면, answer +1 후 cnt 초기화
cnt가 K가 아니라면(작거나, 크다면), cnt를 초기화

### `puzzle[i][j]` 와 `puzzle[j][i]`
for문을 가로 탐색 1개, 세로 탐색 1개 해서 작성했었는데 그냥 인덱스 배열만 바꾸어주면 더 간단히 해결할 수 있었다.

