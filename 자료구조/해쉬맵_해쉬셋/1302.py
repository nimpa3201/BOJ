n = int(input())
li = [input() for _ in range(n)]
d= dict()
ans =[]
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
a= list(d.values())
tmp =max(a)
for i in d:
    if d[i] ==tmp:
        ans.append(i)
ans.sort()
print(ans[0])

