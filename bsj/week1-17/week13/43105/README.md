# 정수 삼각형
## 풀이과정
1. DFS로 풀기
   - 괜히 DP로 풀고 싶지 않아서 시도
      ```python
        # PROGRAMMERS 코딩테스트 연습 > 동적계획법 > 정수 삼각형
        # 43105
        def solution(triangle):
            answer = -float('inf')
            def dfs(total, row, col):
                nonlocal answer
                answer = max(total, answer)

                if row == len(triangle):
                    return
                dfs(total+triangle[row][col], row+1, col)
                dfs(total+triangle[row][col], row+1, col+1)
            dfs(0, 0, 0)

            return answer
      ```
   - 시간초과가 너무 많이 발생하여 DP로 풀이
2. DP로 풀기
      ```python
      # PROGRAMMERS 코딩테스트 연습 > 동적계획법 > 정수 삼각형
      # 43105
      def solution(triangle):
          for i in range(len(triangle)-2, -1, -1):    # 밑 바닥부터 올라와
              for j in range(len(triangle[i])):       # 각 칸 돌아보기
                  # 각 칸은 아래에 깔고 앉은 놈 중 큰 놈이랑 더하기
                  triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
          return triangle[0][0]                       # 꼭대기에 선 놈이 정점
      ```
## DFS보다 DP가 더 빠른 이유
중복된 계산을 피하기 때문이다!
- 경로가 겹치는 경우에도 DFS는 다시 탐색을 하기 때문에 중복된 계산이 발생한다.
- 각 경로에 대해 완전히 독립적인 탐색을 진행하기 때문에 비효율적이다.

DP는 중복 계산을 줄이는 최적화 기법이다. 한번 계산한 값을 저장해두고 다시 사용한다.