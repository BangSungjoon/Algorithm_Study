from itertools import permutations


def check(num):
    if num < 2:
        return False
    else:
        for k in range(2, int(num ** 0.5) + 1):  # 2부터 루트 num까지 나눠보기
            if num % k == 0:
                return False
    return True


def solution(numbers):
    num_list = list(numbers)  # 문자열 리스트
    ans = set()

    for i in range(1, len(num_list) + 1):
        perm = set(permutations(num_list, i))
        print(perm)

        for p in perm:
            number = int(''.join(p))

            if check(number):
                ans.add(number)

    return len(ans)