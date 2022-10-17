from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
cnt=0
def bfs():
    global cnt
    dxs = [1,-1,0,0]
    dys=[0,0,-1,1]
    while q :
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = x+dx
            ny = y+dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1) # 그전 step 수 +1
                

def push(x,y,s):
    visited[x][y] =1
    q.append((x,y))                 #push할때마다 다음 step 배열에 수 넣어줌 
    step[x][y]=s

def can_go(x,y):
    if is_range(x,y) and visited[x][y] ==0 and graph[x][y] ==1:
        return True
    else:
        return False
def is_range(x,y):
    return 0<=x <n and 0<=y<m

push(0,0,1)
visited[0][0]=1
bfs()

print(step[n-1][m-1])