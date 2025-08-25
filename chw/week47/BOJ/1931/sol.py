N = int(input())
meeting_info = [list(map(int, input().split())) for _ in range(N)]
meeting_info.sort()

max_meetings = 0

def meeting(current_time, cnt):
    global max_meetings

    if current_time > meeting_info[-1][0]:
        max_meetings = max(cnt, max_meetings)
        return

    for i in range(len(meeting_info)):
        start, end = meeting_info[i][0], meeting_info[i][1]

        if current_time <= start:
            if cnt + len(meeting_info)-1-i < max_meetings:
                return

            meeting(end, cnt+1)

meeting(0, 0)

print(max_meetings)