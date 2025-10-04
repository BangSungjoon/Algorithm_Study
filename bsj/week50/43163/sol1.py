def solution(begin, target, words):
    answer = 51
    if target not in words:
        return 0
    
    def dfs(word, cnt, target, visi):
        nonlocal answer
        if cnt >= answer:
            # 백트래킹
            return
        if word == target:
            answer = cnt

        for k in range(len(words)):
            if visi[k] == 0:
                difference = 0
                for t in range(len(word)):
                    if word[t] != words[k][t]:
                        difference += 1
                        if difference > 1:
                            break
                if difference == 1:
                    visi[k] = 1
                    dfs(words[k], cnt+1, target, visi)
                    visi[k] = 0
    
    단어수 = len(words)
    for w in range(단어수):
        difference = 0  # 원본과 차이나는 알파벳 수
        for i in range(len(begin)):
            if begin[i] != words[w][i]:
                difference += 1
                if difference > 1:
                    break
        if difference == 1:
            visited = [0]*단어수
            visited[w] = 1
            dfs(words[w], 1, target, visited)
            
    if answer == 51:
        return 0
    
    return answer