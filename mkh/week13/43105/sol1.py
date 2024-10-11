from copy import deepcopy


def solution(triangle):
    # 내려오는 최대값을 저장할 n_triangle
    n_triangle = deepcopy(triangle)
    for i in range(len(triangle)-1):
        for j in range(i+1):
            # 현재까지 내려오면서 쌓인 값 + 그 위치에 있는 값의 최댓값만 그 위치에 남긴다.
            if n_triangle[i+1][j] < n_triangle[i][j]+triangle[i+1][j]:
                n_triangle[i+1][j] = n_triangle[i][j]+triangle[i+1][j]
            # 왼쪽부터 쭉 갱신하고 있으므로 오른쪽은 확인할 필요 없음.
            n_triangle[i + 1][j+1] = n_triangle[i][j] + triangle[i + 1][j+1]
    # 마지막 줄의 max 값만 제출하면 된다.
    return max(n_triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
