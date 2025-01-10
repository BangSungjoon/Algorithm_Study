def solution(name):
    move = 0
    arr = []


    for i in range(len(name)):
        # 알파벳 변경(13번 부터는 뒤에서 세는 게 더 빠름)
        c = ord(name[i]) - ord('A')
        if c <= 13:
            move += c
        else:
            move += (ord('Z') - ord(name[i]))

        # 이동할 배열 생성
        if name[i] == 'A':
            arr.append(i)

    # 1. A밖에 없으면 바로 return
    if len(arr) == 0:
        return
    # 2. 왼 -> 오 쭉
    left_to_right = len(name) - 1






    return arr

name = "AAAAAAAAABBBBB"
print(solution(name))