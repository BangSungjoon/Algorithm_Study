def solution(name, yearning, photo):
    score_dic = dict(zip(name, yearning))  # {name: yearning} 생성
    return [sum(score_dic.get(nm, 0) for nm in p) for p in photo]  # 딕셔너리에 있으면 그 점수를 없으면 0을 반환하기 위해 get 메소드 활용

# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
# print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))