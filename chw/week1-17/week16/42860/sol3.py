def solution(name):
    move = 0
    visited = [0] * len(name)

    for i in range(len(name)):
        # 알파벳 변경(13번 부터는 뒤에서 세는 게 더 빠름)
        c = ord(name[i]) - ord('A')
        if c <= 13:
            move += c
        else:
            move += (ord('Z') - ord(name[i]))

    for j in range(len(name)):
