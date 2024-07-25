
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    arr = []
    
    for col in range(m):
        arr.append(list(map(int, input().split())))
    
    max_sum = -float('inf')
    
    for i in range(m - n + 1):
        current_sum = [0] * (m - n + 1)
        
        for k in range(n):
            for j in range(m - n + 1):
                if k == 0:
                    current_sum[j] = sum(arr[i + k][j:j + n])
                else:
                    current_sum[j] += sum(arr[i + k][j:j + n])
        
        max_sum = max(max_sum, max(current_sum))
    
    print(f"#{test_case} {max_sum}")