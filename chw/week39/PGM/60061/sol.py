def solution(n, build_frame):
    lst = []

    def able(x, y, a):
        if a == 0:  # 기둥
            return (
                y == 0
                or [x, y - 1, 0] in lst
                or [x, y, 1] in lst
                or [x - 1, y, 1] in lst
            )
        else:  # 보
            return (
                [x, y - 1, 0] in lst
                or [x + 1, y - 1, 0] in lst
                or ([x - 1, y, 1] in lst and [x + 1, y, 1] in lst)
            )

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            lst.append([x, y, a])
            if not all(able(q, w, e) for q, w, e in lst):
                lst.remove([x, y, a])  # 조건 불만족 시 취소

        else:       # 삭제
            lst.remove([x, y, a])
            if not all(able(q, w, e) for q, w, e in lst):
                lst.append([x, y, a])  # 조건 불만족 시 복구

    return sorted(lst, key=lambda x: (x[0], x[1], x[2]))