from collections import deque
m,n,k = map(int,input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]
visited =[[ 0 for _ in range(n)] for _ in range(m)]
q = deque()
cnt =0
ans =[]
for _ in range(k):
    c1,r1,c2,r2 = map(int,input().split())
    for i in range(c1,c2):
        for j in range(r1,r2):
            matrix[m-(j+1)][i] =1
def push(x,y):
    q.append((x,y))
    visited[x][y] = True

def can_go(x,y):
    if 0<=x<m and 0<=y<n and not visited[x][y] and matrix[x][y] ==0:
        return True
    else:
        return False

def dfs():
    num=1
    while q:
        x,y = q.popleft()
        dxs,dys = [0,0,1,-1],[-1,1,0,0]
        for dx, dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny)
                num +=1
    ans.append(num)

for i in range(n):
    for j in range(n):
        if can_go(i,j) :
            cnt+=1
            push(i,j)
            dfs()
print(cnt)
ans.sort()
print(*ans)