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
        
        def check_tree(s):
            # 리프 노드일 경우 1이든 0이든 문제 없으니까 항상 True
            if len(s) == 1:
                return True
            # 해당 서브 트리의 루트 노드는 정 중앙에 있는 값이므로 해당 값을 탐색
            mid = len(s)//2
            # 루트 노드가 0이라면 내 아래에 있는 모든 노드들은 0이어야 함. 해당 경우를 만족하는 경우 True
            if s[mid] == '0':
                return all(x == '0' for x in s)
            else:
                # 루트 노드가 0이고 그 아래에 1이 있는 경우를 제외하고선 항상 True
                return check_tree(s[:mid]) and check_tree(s[mid + 1:])
        # return값이 bool이므로 문제의 형태에 맞춰 정수형으로 변환하여 리턴
        numbers[i] = int(check_tree(binary))
    return numbers