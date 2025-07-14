# 백준 용액
n = int(input())
arr = list(map(int, input().split())) # 오름차순으로 주어진다.

result = float('inf')
left, right = 0, n-1
n1, n2 = arr[left], arr[right]

while left < right:     # 왼쪽이 오른쪽을 안넘어가는 동안 반복
    n3 = arr[left] + arr[right]
    if result > abs(n3):
        result = abs(n3)
        n1, n2 = arr[left], arr[right]
    if n3 < 0:          # 합이 0보다 작다면, 왼쪽 값을 오른쪽으로 옮겨 키워준다.
        left += 1
    else:
        right -= 1
        
print(n1, n2)