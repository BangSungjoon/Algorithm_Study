# [G5] 1041 주사위

# STEP 1. 입력 받기
N = int(input())
num = list(map(int, input().split()))

# STEP 2. 계산
if N == 1:
    answer = sum(sorted(num)[:5])       # 가장 작은거 빼기
else:
    answer = 0

    pairs = []
    # 서로 마주보는 숫자 중 작은 값 추가
    pairs.append(min(num[0], num[5]))
    pairs.append(min(num[1], num[4]))
    pairs.append(min(num[2], num[3]))
    pairs.sort()                        # 오름차순 정렬

    # 면이 1/2/3개 보이는 주사위의 면 최소 합
    sum1 = pairs[0]
    sum2 = pairs[0] + pairs[1]
    sum3 = sum(pairs)

    # N개의 면이 보이는 주사위 총 수 * N개의 면 최소 합
    answer += 4 * sum3
    answer += (4*(N-1) + 4*(N-2)) * sum2
    answer += (4*(N-1)*(N-2) + (N-2)*(N-2)) * sum1

print(answer)