# 완전탐색 방식으로 시도(시간 복잡도: O(2^N)

N = int(input())
seq = list(map(int, input().split()))

res = 0

def dfs(idx, inc_seq):
    global res

    # 마지막 숫자까지 확인했으면 길이 갱신
    if idx == N:
        res = max(res, len(inc_seq))
        return

    # 숫자를 수열에 넣거나 빼기
    for i in range(idx, N):
        if inc_seq:
            if inc_seq[-1] < seq[i]:
                dfs(idx+1, inc_seq+[seq[i]])
            else:
                dfs(idx+1, inc_seq)
        else:
            dfs(idx+1, inc_seq+[seq[i]])

dfs(0, [])
print(res)