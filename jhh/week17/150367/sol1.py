# 미완

# numbers
# [7, 42, 5]            # [1, 1, 0]
# [63, 111, 95]         # [1, 1, 0]
def to_binary(num):
    bi_lst = []
    while num > 0:
        bi_lst.append(num % 2)
        num //= 2
    if not len(bi_lst) % 2:
        bi_lst.append(0)
    bi_lst.reverse()
    return bi_lst
# print(to_binary(42))    # [0, 1, 0, 1, 0, 1, 0]

# def preorder(binary, node, cnt):
#     if binary[node] == 0:
#         return
#     current_node = node // 2
#     preorder(binary, current_node-1, cnt+1)
#     preorder(binary, current_node+1, cnt+1)

def preorder(binary, node, cnt):
    if node < 0 or node >= len(binary):  # 노드가 범위를 벗어난 경우 종료
        return cnt
    if binary[node] == 0:  # 현재 노드가 없으면 종료
        return cnt
    cnt += 1  # 현재 노드가 존재하면 cnt 증가
    cnt = preorder(binary, node // 2, cnt)  # 왼쪽 자식 노드
    cnt = preorder(binary, node * 2 - node // 2, cnt)  # 오른쪽 자식 노드

    return cnt

binary = to_binary(7) # [1, 1, 1]
root_node = len(binary) // 2
print(preorder(binary, root_node, 0))

def solution(numbers):
    answer = []
    for i in numbers:
        binary = to_binary(i)
        root_node = len(binary) // 2
        preorder(binary, root_node, 0)
        # 재귀 함수를 통해 1의 개수 확인 -> 총 1의 개수와 맞는지 확인 -> 맞으면 1 출력, 아니면 0 출력

    return answer