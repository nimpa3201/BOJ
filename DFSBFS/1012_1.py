from collections import deque
T = int(input())

def can_go(x,y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y]==1:
        return True
    else:
        return False

def push(x,y):
    global cnt
    q.append((x,y))
    visited[x][y] = 1


def bfs():
    while q:
        x,y = q.popleft()
        dxs = [0,0,-1,1]
        dys = [1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny)

for _ in range(T):
    m,n,k = map(int,input().split())
    grid = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q= deque()
    for _ in range(k):
        v1,v2 = map(int,input().split())
        grid[v2][v1] =1
    
    cnt=0
    for i in range(n):
        for j in range(m):

            if can_go(i,j):
                cnt+=1
                push(i,j)
                bfs()
    print(cnt)