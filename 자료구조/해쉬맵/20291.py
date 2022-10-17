

n = int(input())
file = {}
d= dict()
for _ in range(n):
    file = input().split('.')[1]
    if file not in d:
        d[file] =1
    else:
        d[file]+=1
ans =list(d.keys())
ans.sort()
for i in ans:
    print(i,d[i])