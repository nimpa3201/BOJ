s = input()
target0 = '0' * len(s)
target1 = '1' * len(s)

mismatch = False
ans =0
li=[]
for i in range(len(s)):
    if s[i] != target0[i]:
        if not mismatch :
            ans+=1
            mismatch = True
    else:
        mismatch = False
li.append(ans)
mismatch = False
ans=0
for i in range(len(s)):
    if s[i] != target1[i]:
        if not mismatch:
            ans+=1
            mismatch = True
    else:
        mismatch = False
li.append(ans)
print(min(li))