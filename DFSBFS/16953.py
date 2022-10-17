from collections import deque 
n,m = map(int,input().split())
q =deque([(n,1)])
res =-1


while q:
    x, cnt = q.popleft()
    if x == m:
        res = cnt
        break
    if 2*x <=m:
        q.append((2*x,cnt+1))
    if int(str(x)+'1') <= m:
        q.append((int(str(x)+'1'),cnt+1))

print(res)

