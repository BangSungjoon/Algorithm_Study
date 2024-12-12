def solution(numbers):
    for i in range(len(numbers)):
        # 2진수로 변환
        binary = bin(numbers[i])[2:]
        l = len(binary)
        h = 1

        # 트리의 높이를 찾아서 포화이진트리가 될 때까지 0을 앞에다 채워준다.
        while (2**h-1)<l:
            h += 1
        binary = binary.zfill(2**h-1)

        # 0번을 시작으로 봤을 때 리프노드는 항상 홀수니까 짝수 애들이 0이 아닌지, 0이라면 자식 노드들이 0인지 확인. 자식 노드들이 +- 1인줄
        for j in range(1, l, 2):
            if binary[j] == '0' and (binary[j-1] == '1' or binary[j+1] == '1'):
                numbers[i] = 0
                break
        else:
            numbers[i] = 1
    return numbers