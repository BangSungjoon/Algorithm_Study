# 네트워크
# 네트워크 개수 구하기 (서로 연결된 것을 1개로 본다.)

def solution(n, computers):
    visited = [0] * n # 방문여부 기록리스트
    answer = 0

    for com in range(n): # 모든 컴퓨터 순회
        if visited[com] == 0: # 방문하지 않은 컴퓨터인 경우
            q = [com] 
            visited[com] = 1 # 현재 컴퓨터 방문처리

            while q: # 큐가 빌때까지 무한 반복
                current = q.pop(0) # 큐에서 현재 컴퓨터 추출
                for connect in range(n): # 모든 컴퓨터와 연결 확인
                    if connect !=  current and computers[current][connect] == 1: # 연결된 컴퓨터찾고,
                        if visited[connect] == 0: #방문안했던거라면 방문처리후 큐에 추가
                            visited[connect] = 1 
                            q.append(connect)
            answer += 1    
    return answer                   

test_cases = [
    (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]),
    (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
]

for n, computers in test_cases:
    print(solution(n, computers))        