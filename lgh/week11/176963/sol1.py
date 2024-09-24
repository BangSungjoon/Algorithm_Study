# 추억 점수
def solution(name, yearning, photo):
    answer = []
    for lst in photo: # phto에서 한 행 뽑음
        sum = 0 
        for person in lst: # 한 행에서 한 명씩 순회
            if person in name: # name에 있는 person이라면
                sum += yearning[name.index(person)]  # name배열에서 person의 인덱스만 추출하는 index함수 사용해 점수 더함   
        answer.append(sum)
    return answer