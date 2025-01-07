# 프로그래머스 코딩테스트 연습 > 해시 > 의상
# 42578
def solution(clothes):
    answer = 1
    fashion = []
    for cloth in clothes:
        fashion.append(cloth[1])
    fa = set(fashion)
    for f in fa:
        # 입거나 안입음이기에 +1
        answer *= (fashion.count(f)+1)

    # 아에 다 안입은 경우는 빼줘야 하니 전체에서 -1
    return answer-1