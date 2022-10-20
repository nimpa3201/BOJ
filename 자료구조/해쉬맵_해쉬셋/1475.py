arr = list(map(int,input()))
d= dict()
tmp =0
p=[]
for i in arr:
    if i == 6:
        i =9
    if i in d:
        d[i] +=1
    else:
        d[i] =1

for i in d:
    if d[i] ==max(list(d.values())):
        p.append(i)


if len(p) ==1 and 9 in d and d[9] == max(list(d.values())):
    if 9 in d and d[9]%2 ==0:
        print(d[9]//2)
    else:
        print((d[9]//2)+1)
else:
    print(max(d.values()))