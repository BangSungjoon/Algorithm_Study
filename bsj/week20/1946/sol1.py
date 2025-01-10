# 백준: 신입 사원
# 1차 서류 심사와 2차 서류 심사
for _ in range(int(input())):
    n = int(input())
    vol = [0]*n
    for i in range(n):
        vol[i] = list(map(int, input().split()))
    min_interview = n+1
    cnt = 0     # 합격자 수
    vol.sort()  # 오름차순으로 정렬

    # 오름차순이니 서류 심사 순위는 비교할 필요가 없다.
    # 면접 심사 순위만 비교해 봐
    for i in range(n):
        if vol[i][1] < min_interview:
            cnt += 1
            min_interview = vol[i][1]
    print(cnt)