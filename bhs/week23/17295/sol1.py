n = int(input())
val = list(map(int, input().split()))
nge = [-1]*n
stack = []

for i in range(n):
    input_idx = i
    idx = val[input_idx]

    while stack and val[stack[-1]] < idx:   #스택에 뭐가 있고, 스택에 top값의 인덱스가 더 오른쪽이 될때까지
        nge[stack.pop()] = val

    stack.append(input_idx)

print(*nge) 



