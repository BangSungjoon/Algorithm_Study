def solution(gems):
    gem_type = set()

    for gem in gems:
        gem_type.add(gem)

    min_section = []

    for i in range(len(gems)):
        # print('시작 번호', i)
        type_test = set()
        type_test.add(gems[i])

        if len(type_test) == len(gem_type):
            min_section = [i, i]
            break

        for j in range(i + 1, len(gems)):
            type_test.add(gems[j])
            # print('현재 보석 상황', type_test)

            if len(type_test) == len(gem_type):
                if not min_section:
                    min_section = [i, j]

                # 기록된 섹션의 길이보다 짧으면 교체, 기록된 섹션 길이와 같으면 시작 번호 비교
                if min_section[1] - min_section[0] > j - i:
                    min_section = [i, j]
                elif min_section[1] - min_section[0] == j - i and min_section[0] > i:
                    min_section = [i, j]

                # print('현재 최소 섹션 상황', min_section)

        # print('사이클 돌고 난 후 최소 섹션', min_section)

    return [min_section[0] + 1, min_section[1] + 1]