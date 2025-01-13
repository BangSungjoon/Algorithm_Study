# 백준
# 15903 카드 합체 놀이
# 카드의 개수를 나타내는 n, 카드 합체를 몇 번 하는지 m
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 만들 수 있는 가장 작은 점수를 출력하자.
for _ in range(m):
    # 작은 순으로 정렬
    arr.sort()
    twosome = arr[0] + arr[1]
    arr[0], arr[1] = twosome, twosome

print(sum(arr))