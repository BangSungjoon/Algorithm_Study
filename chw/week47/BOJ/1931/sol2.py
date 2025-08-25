N = int(input())
meeting_info = [list(map(int, input().split())) for _ in range(N)]
meeting_info.sort(key=lambda x: (x[1], x[0]))

time = 0
cnt = 0

for i in range(len(meeting_info)):
    start = meeting_info[i][0]
    end = meeting_info[i][1]

    if time <= start:
        cnt += 1
        time = end

print(cnt)