def solution(record):
    
    # 유저 정보 저장용 딕셔너리
    user_info = {}
    # 기록 리스트
    logs = []
    
    for r in record:
        parts = r.split()
        command = parts[0]
        uid = parts[1]
        
        if command == "Enter":
            nickname = parts[2]
            user_info[uid] = nickname
            logs.append((uid,"Enter"))
            
        elif command == "Leave":
            logs.append((uid, "Leave"))
            
        elif command == "Change":
            nickname = parts[2]
            user_info[uid] = nickname
            
    result = []
    for uid, action in logs:
        nickname = user_info[uid]
        if action == "Enter":
            result.append(f"{nickname}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{nickname}님이 나갔습니다.")
            
    return result