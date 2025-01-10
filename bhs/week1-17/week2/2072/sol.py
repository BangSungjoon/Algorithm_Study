T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    odd_sum = sum(num for num in numbers if num % 2 != 0)

    print(f"#{t} {odd_sum}")