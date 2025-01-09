def ymd_date(date_str):
    if len(date_str) != 8:
        return False
    
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])
    
    if month < 1 or month > 12:
        return False
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day < 1 or day > days_in_month[month]:
        return False
    
    return True

T = int(input())
for t in range(1, T + 1):
    date = input().strip()
    
    if ymd_date(date):
        f_date = f"{date[:4]}/{date[4:6]}/{date[6:]}"
        print(f"#{t} {f_date}")
    else:
        print(f"#{t} -1")