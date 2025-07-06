N, K = map(int, input().split())    # 수빈 N, 동생 K

def find(subin, baby, cnt):
    global res

    # 동생 찾았을 때
    if subin == baby:
        res = min(res, cnt)
        return cnt

    # 음수로는 못 감
    if subin < 0:
        return

    if visited[subin] == 0:
        visited[subin] = 1
        find(subin + 1, baby, cnt + 1)
        find(subin - 1, baby, cnt + 1)
        find(subin * 2, baby, cnt + 1)
    else:
        return

res = 1e9
visited = [0]*100000
find(N, K, 0)
print(res)