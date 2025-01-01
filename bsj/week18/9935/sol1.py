# 백준
# 문자열 폭발

string = input()
bomb = input()
bomb_len = len(bomb)  # 폭발 문자열의 길이
stack = []

for char in string:
    stack.append(char)
    # 스택의 마지막 부분이 폭발 문자열과 일치하는지 확인
    if ''.join(stack[-bomb_len:]) == bomb:  # 인덱스 슬라이싱은 범위를 벗어나도 오류가 생기지 않는다.
        # 폭발 문자열 제거
        del stack[-bomb_len:]

# 스택에 남은 결과를 출력
result = ''.join(stack)
print(result if result else "FRULA")