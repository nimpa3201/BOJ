s = input()
li = list(s)
n = int(input())
cmd = [tuple(input().split()) for _ in range(n)]
a= len(li)-1
for m in cmd:
    if m[0] =='L':
        a=-1

    if m[0] =='D':
        a+=1

    if m[0]=='B':
        del li[a]
        a=-1
        

    if m[0]=='P':
        li.insert(a,m[1])
print(li)