def solution(str1, str2):
    new_str1 =[]
    new_str2 =[]
    # str1을 입력받아와서 알파벳이면 2개씩 슬라이싱해서 new_str1에 넣어줌 
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            new_str1.append(str1[i:i+2])
    # str2을 입력받아와서 알파벳이면 2개씩 슬라이싱해서 new_str2에 넣어줌 
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
           new_str2.append(str2[i:i+2]) 
    # new_str1을 소문자로 바꿔줌
    for i in range(len(new_str1)):
        new_str1[i] = new_str1[i].lower()
    
    # new_str2를 소문자로 바꿔줌
    for i in range(len(new_str2)):
        new_str2[i] = new_str2[i].lower()
 
    #new_str2를 지워나가면서 교집합의 개수를 셀 것이므로, 미리 복사해둠 
    copy_new_str2 = new_str2.copy()
    intersection = 0  #교집합 개수

    # new_str1에 담긴 문자열이 new_str2에 있다면 하나씩 지울때마다 교집합 개수 +1
    for str in new_str1:
        if str in new_str2:
            copy_new_str2.remove(str)
            intersection += 1
    #합집합 
    union = len(new_str1) + len(new_str2) - intersection
    
    #0나누기0은 1로 처리되므로 ans지정
    if intersection == 0 and union==0:
        ans = 65536 
    else:
        ans=int((intersection / union) * 65536 ) 
    return ans

    #sdf