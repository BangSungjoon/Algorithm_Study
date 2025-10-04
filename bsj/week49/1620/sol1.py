# [백준] 나는야 포켓몬 마스터 이다솜
n, m = map(int, input().split())
poke = []
for _ in range(n):
    name = input()
    poke.append(name)

for _ in range(m):
    problem = input()
    if problem.isnumeric():
        print(poke[int(problem)-1])
    else:
        print(poke.index(problem)+1)