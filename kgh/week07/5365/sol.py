import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sentence = [list(input()) for _ in range(5)]
    max_len = max(len(sen) for sen in sentence)

    result = ''
    for i in range(max_len):
        for j in range(5):
            if len(sentence[j]) > i:
                result += sentence[j][i]
    print(f'#{tc} {result}')