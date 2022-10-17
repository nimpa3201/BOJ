from collections import deque
n,k =map(int,input().split())
q =deque()
li=[]
for i in range (1,n+1):
    q.append(i)
cnt =1
while q :
    if cnt < k:
        cnt+=1
        a =q.popleft()
        q.append(a)
    if cnt ==k:
        cnt =1
        b=q.popleft()
        li.append(b)

print('<',end='')
for i in li[:-1]:
    print(i,end =', ')
print(li[-1],end ='')
print(">")