'''
각 종류별 경우의 수 : 종류 수 + 1(안입는거)
'''
def solution(clothes):
    # 옷의 종류만 담은 리스트
    types = [clothe[1] for clothe in clothes]
    answer = 1
    # 유니크한 값으로 이루어진 리스트 순회
    for type in set(types):
        # 각 옷의 횟수 + 1 값을 곱해나감
        answer *= (types.count(type) + 1)
    # 아무것도 입지 않는 경우 제외
    return answer - 1


# 결과 출력
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))