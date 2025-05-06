from collections import deque

def solution(begin, target, words):
    # 불가능한 경우
    if target not in words:
        return 0

    answer = 1e9

    q = deque([(begin, 0)])
    visited = set()

    while q:
        current, cnt = q.popleft()

        if current == target:
            if answer > cnt:
                answer = cnt
                break

        for word in words:
            # 다른 단어 수 체크
            diff = 0
            for w in range(len(word)):
                if diff > 1:
                    break
                if current[w] != word[w]:
                    diff += 1

            # 딱 1개만 다르면 큐에 추가
            if diff == 1 and word not in visited:
                q.append((word, cnt+1))
                visited.add(word)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
ans = solution(begin, target, words)
print(ans)