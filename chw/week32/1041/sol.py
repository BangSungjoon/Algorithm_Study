from itertools import combinations

N = int(input())
num_list = list(map(int, input().split()))
A, B, C, D, E, F = num_list

if N == 1:
    print(sum(num_list) - max(num_list))
else:
    res = 0

    # 1개 고르는 경우
    one = min(num_list)
    res += one * ((N-2) * (N-2) * 5 + (N-2) * 4)

    # 2개 고르는 경우
    two_list = list(combinations(range(6), 2))
    two = 1e9
    for comb in two_list:
        # 마주 보는 면의 조합은 제외
        if comb == (5,0) or comb == (0,5):
            continue
        elif comb == (2,3) or comb == (3,2):
            continue
        elif comb == (1,4) or comb == (4,1):
            continue
        else:
            if two > num_list[comb[0]] + num_list[comb[1]]:
                two = num_list[comb[0]] + num_list[comb[1]]
    res += two * ((N-2) * 8 + 4)

    # 3개 고르는 경우
    first = min(A, F)
    second = min(B+C, B+D, D+E, E+C)
    three = first + second
    res += three * 4

    print(res)