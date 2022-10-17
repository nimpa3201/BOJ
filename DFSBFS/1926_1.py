from collections import deque
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
def can_go(x,y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] ==1:
        return True
    else:
        return False
def push(x,y):
    q.append((x,y))
    visited[x][y] =1
def bfs():
    global cnt
    while q:
        x,y = q.popleft()
        dxs = [0,0,1,-1]
        dys = [-1,1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                cnt+=1
                push(nx,ny)
ans =[]
for i in range(n):
    for j in range(m):
        cnt=0
        if can_go(i,j):
            cnt+=1
            push(i,j)
            bfs()
            ans.append(cnt)
if len(ans) ==0:
    print(0)
    print(0)
else:
    print(len(ans))
    print(max(ans))