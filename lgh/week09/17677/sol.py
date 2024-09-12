

str1 = 'FRANCE'
str2 = 'french'
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
print(new_str1)   
# new_str2를 소문자로 바꿔줌
for i in range(len(new_str2)):
    new_str2[i] = new_str2[i].lower()
print(new_str2)

copy_new_str2 = new_str2.copy()
# new-str1에 담긴 문자열과 new_str2에 담긴 문자열을 비교해서 개수를 세야하는ㄴ데.
#각 문자열의 중복 개수를 세야함->딕셔너리? 그리고,, 최소 중복과 최대중복의 개수를 세야함.
intersection = 0
for str in new_str1:
    if str in new_str2:
        copy_new_str2.remove(str)
        intersection += 1

union = len(new_str1) + len(new_str2) - intersection

if intersection == 0 and union==0:
    ans = 65536 
else:
    ans=int((intersection / union) * 65536 ) 
print(ans)