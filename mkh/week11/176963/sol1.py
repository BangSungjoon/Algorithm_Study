def solution(name, yearning, photo):
    answer = []
    for members in photo:
        sum = 0
        for member in members:
            if member in name:
                sum += yearning[name.index(member)]
        answer.append(sum)
    return answer