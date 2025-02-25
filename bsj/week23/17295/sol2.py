# 오큰수 스택 버전으로 풀기
# 전체 리스트를 순회할거고 stack은 오큰수를 배정 받을 index 대기방
n = int(input())
arr = list(map(int, input().split()))
result = [-1]*n # 결과는 -1로 초기값
stack = []

for i in range(n):
    # 오큰수를 배정 받을 index가 존재하고,
    # 그 index번째의 arr 값이 현재 arr 값 보다 작다면
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i) # 나도 이제 배정 받을래

print(*result)