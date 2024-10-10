'''
최대 던전의 수가 8개로 매우 짧음 (엄청 많은게 아님 -> 완전탐색)
DFS, BFS, 순열조합
'''

from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)  # 던전의 개수
    max_cnt = 0  # 탐험 가능한 최대 던전 수
    for perm in permutations(range(N)):
        # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        remain_k = k  # 초기피로도 설정
        cnt = 0  # 탐험한 던전 수
        # 순열대로 던전을 하나씩 탐험
        for i in perm:
            min_required, fatigue = dungeons[i]  # 최소 피로도와 소모 피로도
            if remain_k >= min_required:  # 탐험 가능이면 (현재 남은 피로도가 던전의 최소 필요 피로도보다 크거나 같아야지)
                remain_k -= fatigue  # 남은 피로도를 소모 피로도만큼 깎아
                cnt += 1  # 탐험한 던전 수 증가
            else:  # 더 탐험 못하면
                break  # 반복문 종료
        # 이번 순서에서 탐험한 던전 수와 기존의 최대 탐험 던전 수 중 더 큰 값
        max_cnt = max(max_cnt, cnt)
    return max_cnt


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
