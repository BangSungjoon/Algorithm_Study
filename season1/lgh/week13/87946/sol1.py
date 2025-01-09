# 87946 피로도
# [[최소 필요 피로도],[소모 피로도]] 
# 가능한 모든 순열을 생성해 순회.(던전을 탐험하는 순서의 모든 경우의 수 순회) 

from itertools import permutations

def solution(k, dungeons):
    answer = 0 # 탐험할 수 있는 최대던전수 초기화
    N = len(dungeons) # 던전의 개수

    for permut in permutations(dungeons, N): # dungeons리스트의 모든 순열을 생성(6개) / 예시 permut = ((30, 10), (50, 20), (20, 5))
       
        count = 0 # 탐헐할 던전 수 초기화
        current_k = k  # 현재의 체력을 저장하는 변수
        for pm in permut: #permute 리스트 내부 리스트 순회 / 예시 pm = (30, 10)
            if current_k >= pm[0]: # 현재 체력이 최소 필요 피로도보다 크거나 같으면
               current_k -= pm[1]  # 소모 피로도 빼줌
               count += 1  # 탐헐한 던전 수 증가
        
        if count > answer:  # 현재 순열에서 탐험한 던전 수가 이전 최대값보다 크면
            answer = count    # 최대 탐험 수를 업데이트

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))
 