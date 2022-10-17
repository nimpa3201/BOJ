from collections import deque
m,n =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
ans =0
def push(x,y,s):
    q.append((x,y))
    visited[x][y] = True
    step[x][y] = s

def can_go(x,y):
    if 0<=x<n and 0<=y<m and not visited[x][y] and arr[x][y] !=-1:
        return True
    else:
        return False


def bfs():
    while q:
        x,y = q.popleft()
        dxs,dys = [0,0,1,-1],[1,-1,0,0]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

for i in range(n):
    for j in range(m):
        if arr[i][j] ==1:
            push(i,j,0)

bfs()

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and arr[i][j] !=-1:
            print(-1)
            exit()
       
        ans = max(ans,step[i][j])

print(ans)
