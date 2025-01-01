# 외계인의 기타 연주
# 손가락 무제한이요
# 6개의 줄
# P개의 프렛 ||||||
# 멜로디에 포함되어 있는 음의 수 N
# 한 줄에 있는 프렛의 수 P
# 8, 10, 12, 12때기, 10 때고, 8때고, 5누르기
N, P = map(int, input().split())
result = 0  # 정답
line = [[0] for _ in range(6)]
for i in range(N):
    li, pr = map(int, input().split())
    # 만약 처음 잡는 줄이거나, 연주한 적이 있지만 더 높은 줄이라면
    if pr > line[li-1][-1]:
        result += 1
        line[li-1].append(pr)
    elif pr < line[li - 1][-1]:
        while line[li - 1] and line[li - 1][-1] > pr:
            line[li - 1].pop()  # 손 떼기
            result += 1
        # 손을 뗀 후, 현재 프렛과 동일한 값이 없다면 새로운 프렛 추가
        if line[li - 1][-1] != pr:
            line[li - 1].append(pr)
            result += 1

print(result)