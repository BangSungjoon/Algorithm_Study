# [백준] 별 찍기 - 10
def make_star(num):
    if num == 3:
        return ['***', '* *', '***']
    pre_star = make_star(num // 3)
    answer = []

    # 1단계
    for star in pre_star:
        answer.append(star * 3)
    # 공백이 들어간 2단계
    for star in pre_star:
        answer.append(star + " "*(num//3) + star)
    # 3단계
    for star in pre_star:
        answer.append(star * 3)

    return answer

n = int(input())
result = make_star(n)

for r in result:
    print(r)