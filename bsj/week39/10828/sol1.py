# 백준 스택
def push(x):
    arr.append(x)

def pop():
    if arr:
        x = arr.pop()
        print(x)
    else:
        print(-1)

def size():
    print(len(arr))

def empty():
    if arr:
        print(0)
    else:
        print(1)

def top():
    if arr:
        print(arr[-1])
    else:
        print(-1)

n = int(input())
arr = []
for _ in range(n):
    command = input().strip().split()
    if len(command) > 1:
        order = command[0]
        num = int(command[1])
        if order == "push":
            push(num)
    else:
        order = command[0]

        if order == "pop":
            pop()
        elif order == "size":
            size()
        elif order == "empty":
            empty()
        elif order == "top":
            top()