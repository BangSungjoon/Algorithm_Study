#코드에 쓰인 개념들 특히 zip()에 대한 공부 더 필요,,,
#리스트 컴프리헨션:[list(reversed(col)) for col in zip(*matrix)]기존의 for 루프를 한 줄로 압축해 리스트 생성
# zip(*matrix)로 행렬을 전치(행과열을 서로 바꿈)하고, 각 행을 뒤집어 90도 회전 효과를 얻음
# zip(*matrix) 함수를 사용해 행렬의 각 행을 언패킹하여 zip 함수의 인자로 전달. 원래 행렬의 각 열이 새로운 행으로...
#reversed() 함수: 시퀀스를 역순으로, 즉 리스트 거꾸로
#슬라이싱: row[::-1]와 matrix[::-1]로, 리스트의 요소들을 역순으로 접근시 사용
#[start:end:step] 형식에서 step을 -1로 주면 역순이 된다.
#map() 함수: map(int, input().split())와 같이 주어진 함수를 반복 가능한 객체의 모든 요소에 적용
#join() 메서드: 하나로 결합
#1961

import sys
sys.stdin = open("input.txt", "r")

def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return list(reversed(list(zip(*matrix))))

def print_rotations(matrix):
    rot_90 = rotate_90(matrix)
    rot_180 = rotate_180(matrix)
    rot_270 = rotate_270(matrix)
    
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    print(f"#{test_case}")
    print_rotations(matrix)