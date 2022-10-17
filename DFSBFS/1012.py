from collections import deque
T = int(input())
    
def bfs(y,x):
    q.append((y,x))
    grid[y][x] =0
    while q:
        y,x = q.popleft()
        dxs = [0,0,1,-1]
        dys = [1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = x+dy
            if nx<0 or nx >=n or ny < 0 or ny >=m:
                continue
            if grid[ny][nx] ==1:
                q.append((ny,nx))
                grid[ny][nx]=0  
             


                

for _ in range(T):
    cnt=0
    n,m,k=map(int,input().split())
    grid = [[0 for _ in range(n)] for _ in range(m)]
    q = deque()
    for _ in range(k):
        v1,v2 = map(int,input().split())
        grid[v2][v1] =1

    for i in range(n):
        for j in range(m):
            if grid[j][i] ==1:
                bfs(j,i)
                cnt+=1
    print(cnt)