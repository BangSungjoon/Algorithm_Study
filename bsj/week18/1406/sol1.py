# 백준
# 에디터

# 문자열 입력 받기
word = input()  # 초기 문자열
n = len(word)

# 스택으로 구현
left_stack = list(word)  # 커서 왼쪽 문자들
right_stack = []         # 커서 오른쪽 문자들

# 명령 받기
for _ in range(int(input())):
    order = input()
    if order[0] == 'P':  # 문자 삽입
        _, char = order.split()
        left_stack.append(char)
    elif order[0] == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())
    elif order[0] == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())
    elif order[0] == 'B':  # 문자 삭제
        if left_stack:
            left_stack.pop()

# 결과 출력
result = ''.join(left_stack + right_stack[::-1])
print(result)