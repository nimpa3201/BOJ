from sys import maxsize


n = int(input())
arr =[int(input()) for _ in range(n)]
d =dict()
ans =maxsize
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
k =max(d.values())
for i in d:
    if d[i] ==k:
        ans = min(ans,i)
print(ans)