# 조이스틱
# 조이스틱 조작횟수 = 알파벳이 A가 아닐 때 변경횟수(상하) + 커서 이동횟수(좌우)


def solution(name):
    alphabet_change = 0 # 알파벳바꾸는 것 상하로 움직임
    cursor_move = len(name) - 1   # 커서를 좌우로 움직임, 최대치가 문자열을 한번 순회하는 것임. 일단 최대치로 설정해놓고 나중에 min값 찾기..

    for alphabet in name: #  상하 움직임(알파벳 바꾸기)
        if (alphabet != 'A'):
            alphabet_change +=  min(ord(alphabet) - ord('A'),  ord('Z') - ord(alphabet) + 1) # A부터 오름차순으로 알파벳찾기 또는 Z부터 내림차순으로 알파벳찾기(Z는+1)      
           
#커서 이동 횟수를 모르겠음


    answer =  alphabet_change + cursor_move
    return answer


