n, m= map(int,input().split())
arr = [str(i) for i in range(1,n+1)]
d = dict()
for num in arr:
    for j in num:
        if j not in d:
            d[j] =1
        else:
            d[j] +=1
print(d[str(m)])