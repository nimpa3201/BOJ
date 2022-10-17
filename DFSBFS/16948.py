from collections import deque
n = int(input())
r1,c1,r2,c2 = map(int,input().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

def can_go(x,y):
    if 0<=x<n and 0<=y<n and not visited[x][y]:
        return True
    else:
        return False


def bfs():
    while q:
        x,y = q.popleft()
        dxs = [-2,-2,0,0,2,2]
        dys = [-1,1,-2,2,-1,1]
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

def push(x,y,s):
    q.append((x,y))
    visited[x][y] = 1
    step[x][y] = s

push(r1,c1,0)
bfs()
print(step[r2][c2] if visited[r2][c2] !=0 else -1)