from itertools import combinations
dungeons = [[80,20],[50,40],[30,10]]
# print(list(combinations(dungeons, len(dungeons))))
def solution(k, dungeons):
    # answer = -1
    max_num = 0
    for combi in combinations(dungeons, len(dungeons)):
        for i in range(len(combi)):
            cnt = 0
            for j in range(len(combi[i])):
                if k >= combi[i][j][0]:
                    cnt += 1
                    k -= combi[i][j][1]
                else:
                    max_num = max(max_num, cnt)
                    break
    return max_num

# 생각은 순열로 해놓고 조합을 import 해버렸따 우헤헤