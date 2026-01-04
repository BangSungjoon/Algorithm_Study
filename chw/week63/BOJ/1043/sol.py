N, M = map(int, input().split())            # 사람 수, 파티 수
truth = list(map(int, input().split()))     # [진실 아는 사람 수, 진실 아는 사람 번호들..]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]   # 파티들

truth_people = set(truth[1:])   # 진실을 들은 사람들
truth_people_len = len(truth_people)

check = 0

# 진실을 들은 사람들이 더 추가되지 않을 때까지 반복
while check != truth_people_len:
    check = truth_people_len

    # 파티에 진실을 아는 사람이 한 명이라도 있으면 파티 전체를 업데이트
    for party in parties:
        if truth_people.intersection(party):
            truth_people.update(party)
            truth_people_len = len(truth_people)

tell_lie = 0     # 거짓말 한 횟수
for party in parties:
    if not truth_people.intersection(party):
        tell_lie += 1

print(tell_lie)