# [[G4] 2636 치즈](https://www.acmicpc.net/problem/2636)


## 관련 개념  
- [BFS](https://github.com/amazingchawon/TIL/blob/master/Algorithm/BFS.md)

## 시간 복잡도
- 매 라운드마다 BFS로 외부 공기를 탐색하며,
- 전체 격자를 최대 r * c번 순회 → O(r * c * 시간)
- 치즈가 매 시간 최소 1개는 녹으므로, 시간은 최악의 경우 r * c