# [백준] 짐 챙기는 숌
n, m = map(int, input().split())    # n 책의 개수, m 박스에 넣을 수 있는 최대 무게
if n == 0:
    print(0)
    exit()
books = list(map(int, input().split()))
box = 0
cnt = 1

for book in books:
    if box + book <= m:
        box += book
    else:
        cnt += 1
        box = book

print(cnt)