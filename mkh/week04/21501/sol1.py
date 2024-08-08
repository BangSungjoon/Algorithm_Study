A = list(range(1, 13))
T = int(input())
subsets = [[]]
#모든 서브셋 구하기
for num in A:
    size = len(subsets)
    # 기존에 있는 리스트의 길이만큼 순회해서 각 리스트에 아이템이 있는 값을 추가 할당하기
    for y in range(size):
        subsets.append(subsets[y]+[num])

for tc in range (1, T+1):
    size, tsum = map(int,input().split())
    # 타겟 사이즈의 subset만 구하기
    subset = [subset for subset in subsets if len(subset)==size]
    c = 0
    for ls in subset:
        #subset의 합 구하기용 변수
        nsum = 0
        for item in ls:
            nsum += item
        #subset의 합이 targetsum과 같으면 count에 1 추가
        if nsum == tsum:
            c += 1

    print(f'#{tc} {c}')
