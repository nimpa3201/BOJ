
s=input()
p=input()
char=dict()

# 각 문자에 대한 index 저장
for i in range(len(s)):
    char[s[i]]=char.get(s[i],i)

print(char)





# for s in S:
#     for p in P:
