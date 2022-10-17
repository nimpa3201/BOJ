n, m = map(int,input().split())
d = dict()
arr = [input() for _ in range(n+m)]
ans =[]
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for i in d :
    if d[i] ==2:
        ans.append(i)
ans.sort()
print(len(ans))
for i in ans:
    print(i)