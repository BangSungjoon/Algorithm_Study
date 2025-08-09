from collections import deque


def solution(game_board, table):
    # 퍼즐 조각 or 빈 공간 찾기
    def bfs(board, target_value):
        pieces = []
        visited = [[0] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == target_value and visited[i][j] == 0:
                    piece = []
                    q = deque([(i, j)])
                    visited[i][j] = 1

                    while q:
                        x, y = q.popleft()
                        piece.append((x, y))

                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == target_value and \
                                    visited[nx][ny] == 0:
                                q.append((nx, ny))
                                visited[nx][ny] = 1

                    pieces.append(transform(piece))

        return pieces

    # 가장 작은 인덱스를 기준으로 상대적 위치 저장
    def transform(piece):
        transformed_piece = []

        min_x = min(x for x, y in piece)
        min_y = min(y for x, y in piece)

        for x, y in piece:
            transformed_piece.append((x - min_x, y - min_y))

        return sorted(transformed_piece)

    # 90도 회전: (x, y) → (y, -x)
    def rotate(piece):
        rotated = [(y, -x) for x, y in piece]
        return transform(rotated)

    # 4가지 회전한 조각 생성
    def get_all_rotations(piece):
        rotations = [piece]
        current = piece

        for _ in range(3):
            current = rotate(current)
            rotations.append(current)

        return rotations

    def test(space):
        for i in range(len(pieces)):
            # 이미 사용한 조각 건너뛰기
            if pieces[i] == 0:
                continue

            rotated_pieces = get_all_rotations(pieces[i])

            for rotated_piece in rotated_pieces:
                if space == rotated_piece:
                    pieces[i] = 0
                    return len(rotated_piece)  # 집어넣은 조각의 수 반환

        return 0

    pieces = bfs(table, 1)
    empty_spaces = bfs(game_board, 0)

    answer = 0

    for space in empty_spaces:
        answer += test(space)
    return answer