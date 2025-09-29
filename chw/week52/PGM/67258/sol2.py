def solution(gems):
    total_gem_type = len(set(gems))
    n = len(gems)

    min_section = [0, len(gems)]

    start = 0
    end = 0

    gem_dict = {}
    gem_dict[gems[start]] = 1
    cnt = 1

    while start < n and end < n:
        # print('현재 상황', start, end, gem_dict)

        if cnt < total_gem_type:
            end += 1

            if end == n:
                break

            if gems[end] in gem_dict:
                gem_dict[gems[end]] += 1
            else:
                gem_dict[gems[end]] = 1
                cnt += 1
        elif cnt == total_gem_type:
            if min_section[1] - min_section[0] > end - start:
                min_section = [start, end]
            elif min_section[1] - min_section[0] == end - start and min_section[0] > start:
                min_section = [start, end]

            gem_dict[gems[start]] -= 1

            if gem_dict[gems[start]] == 0:
                gem_dict.pop(gems[start])
                cnt -= 1

            start += 1

        # print('현재 최소 섹션', min_section)

    return [min_section[0] + 1, min_section[1] + 1]