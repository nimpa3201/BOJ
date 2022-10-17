from collections import deque

n = int(input())

def push(x,y,s) :
    q.append((x,y))
    visited[x][y] = 1
    step[x][y] =s

def can_go(x,y):
    global k
    if 0<=x<k and 0<=y<k and not visited[x][y]:
        return True
    else:
        return False

def bfs():
    while q:
        x,y = q.popleft()
        dxs = [-2, -2, -1, -1,  1, 1,  2, 2]
        dys = [-1,  1, -2,  2, -2, 2, -1, 1]
        for dx, dy in zip(dxs,dys):
            nx = x+dx
            ny = y+ dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)

for _ in range(n):
    k = int(input())
    visited = [[0 for _ in range(k)] for _ in range(k)]
    step = [[0 for _ in range(k)] for _ in range(k)]
    q =deque()
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())

    push(r1,c1,0)
    bfs()
    print(step[r2][c2])