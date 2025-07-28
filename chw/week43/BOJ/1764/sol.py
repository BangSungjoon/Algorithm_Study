import sys
input = sys.stdin.readline


N, M = map(int, input().split())
not_heard = [input().strip() for _ in range(N)]
not_seen = [input().strip() for _ in range(M)]

not_heard = set(not_heard)
not_seen = set(not_seen)

not_heard_seen = not_heard & not_seen

print(len(not_heard_seen))

not_heard_seen = sorted(list(not_heard_seen))

for name in not_heard_seen:
    print(name)