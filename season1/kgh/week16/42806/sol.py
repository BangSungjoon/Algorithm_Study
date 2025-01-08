def solution(name):
    # 알파벳 변경 횟수
    move_cnt = sum(min(ord(n)-ord('A'), ord('Z')-ord(n)+1) for n in name)
    n = len(name)  # 이름의 길이
    min_move = n - 1  # 기본 값 : 오른쪽 끝까지 이동

    # i 위치에서 커서를 양쪽으로 탐색
    for i in range(n):
        next_index = i+1  # 다음으로 비어있지 않은 문자 위치 찾기

        # 연속된 A가 있으면 pass -> next_index 업데이트해 이동 최소화
        while next_index < n and name[next_index] == 'A':
            next_index += 1

        # 두 가지 이동 방식 중 최소 선택
        min_move = min(min_move, i+i+n-next_index, 2*(n-next_index)+i)

        '''
        1) i+i+n-next_index
          - 현재 위치에서 오른쪽 끝으로 이동한 뒤, 다시 돌아와서 마지막 비어있지 않은 위치로 이동
        2) 2*(n-next_index)+i
          - 끝까지 가서 반대로 돌아오는 방식
        '''
    return move_cnt + min_move
