n =int(input())
vill = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt=0
cntList =[]
def is_range(x,y):
    return 0<=x<n and 0<=y<n
 
def can_go(x,y):
    if is_range(x,y) and visited [x][y] ==0 and vill[x][y]!=0:
        return True
    else:
        return False

def dfs(x,y):
    global cnt
    visited[x][y]=1
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if can_go(nx,ny) :
            dfs(nx,ny)
            cnt+=1


for i in range(n):
    for j in range(n):
        if can_go(i,j):
            cnt=1
            visited[i][j] = 1
            dfs(i,j)
            cntList.append(cnt)
cntList.sort()
print(len(cntList))
for i in cntList:
    print(i)