# [백준] 좌표 압축

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))

dic = {arr2[i]: i for i in range(len(arr2))}
answer = [dic[arr[i]] for i in range(n)]

print(" ".join(map(str, answer)))