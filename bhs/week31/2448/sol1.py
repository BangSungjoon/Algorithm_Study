import sys

# 재귀로 풀이

def tri(n):
    if n == 3:
        return[
            "  *  ",
            " * * ",
            "*****"
        ]
    
    s_tri = tri(n//2)
    result = []

    # 상단 부분에 작은 패턴을 가운데 배치하도록 공백
    for line in s_tri:
        make_line = ' ' * (n//2) + line + ' ' * (n//2)
        result.append(make_line)

    # 하단에 작은 패턴들 사이에 공백 추가
    for line in s_tri:
        make_tri = line + ' ' + line
        result.append(make_tri)

    return result

n = int(sys.stdin.readline())

pattern = tri(n)



for line in pattern:
        print(line)