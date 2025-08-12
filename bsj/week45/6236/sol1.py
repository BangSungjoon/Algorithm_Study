# [백준] 용돈 관리
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
# 최소 금액 = 지출 예정 중 가장 큰 금액
# 최대 금액 = 금액의 총 합
start = max(arr)
end = sum(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1     # 인출 한 횟수
    total = mid # 손에 들고 있는 잔액

    for i in range(n):
        if total >= arr[i]:
            # 잔액이 그날 소비 예정 금액보다 많다면
            total -= arr[i]
        else:
            # 잔액이 그날 소비 예정 금액보다 적다면
            cnt += 1
            total = mid - arr[i]

    if cnt > m:
        # 목표한 횟수보다 뽑아 쓴 횟수가 더 많다면
        # 인출한 금액이 작았단 소리임
        start = mid + 1
    else:
        # 목표한 횟수보다 뽑아 쓴 횟수가 같거나 적다면
        # 인출한 금액으로 충분했다는 소리
        end = mid - 1
        answer = mid    # 일단 저장

print(answer)