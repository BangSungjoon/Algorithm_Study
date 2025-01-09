def solution(n, arr1, arr2):
    return [bin(n1|n2)[2:].zfill(n).replace('1','#').replace('0',' ') for n1, n2 in zip(arr1,arr2)]