# musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로,
# 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열
def change_m(musicinfos):
    n_musicinfos = musicinfos.split(',')
    h_m = (int(n_musicinfos[1][:2]) - int(n_musicinfos[0][:2]))*60
    m = int(n_musicinfos[1][3:]) - int(n_musicinfos[0][3:])
    return h_m + m

def solution(m, musicinfos):
    for k in range(len(musicinfos)):
        info = musicinfos[k]
        n=i=0
        result=[]
        my_str = info.split(',')[3]
        num = change_m(info)
        # 재생된 음악
        while n < num:
            if i >= len(my_str):
                i %= len(my_str)
            else:
                if i == len(my_str)-1 and my_str[-1] != '#':
                    result.append(my_str[i])
                    i += 1
                    n += 1
                else:
                    if my_str[i+1] != '#':
                        result.append(my_str[i])
                        i += 1
                        n += 1
                    else:
                        result.append(my_str[i:i+2])
                        i += 2
                        n += 1
        # 기억하는 멜로디 정보
        new_m = []
        i = 0
        while i < len(m):
            if i == len(m)-1:
                new_m.append(m[i])
                i += 1
            else:
                if m[i+1] != '#':
                    new_m.append(m[i])
                    i += 1
                else:
                    new_m.append(m[i:i+2])
                    i += 2
        # 멜로디가 있으면 반환
        for i in range(num-len(new_m)):
            count = 0
            for j in range(len(new_m)):
                if new_m[j] == result[i+j]:
                    count += 1
            if count == len(new_m):
                return info.split(',')[2]

    # 없으면 None 반환
    return '(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

print(len(["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(["A", "B"] in ['C#', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D', 'E', 'F', 'G', 'A', 'B'])

# "ABCDEFG"
# ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "HELLO"
#
# "CC#BCC#BCC#BCC#B"
# ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# "FOO"
#
# "ABC"
# ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# "WORLD"

