'''
초기값이 A들이므로 ord 값으로 치환하여 (기존 A값) 65와 (A를 아래로 한번 내리면 Z임을 감안한 숫자) 91과의 차이 중
더 작은 값으로 해당 칸에서 해당 글자를 만드는 이동 횟수를 구함.
'''


def solution(name):
    int_name = [min(ord(char) - 65, 91 - ord(char)) for char in name]
    answer = sum(int_name)
    
    togos = [index for index, char in enumerate(name) if char != 'A']    
    n = len(name)
    
    if togos:
        move = n-1
        for i in range(len(togos)):
        # togo의 i번째 인덱스까지 갔다가 뒤로 돌아오는 경우 vs. i+1번째 인덱스까지 갔다가 앞으로 돌아오는 경우
            if i == len(togos)-1:
                new_move = togos[i]
            else:
                new_move = min(2*togos[i]+n-togos[i+1], togos[i] + 2*(n-togos[i+1]))
            if move > new_move:
                move = new_move
        answer += move
    else:
        answer = 0
    
    
    return answer
