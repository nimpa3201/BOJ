import sys
sys.setrecursionlimit(10**5)

n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
rain= max(max(arr))
cnt=0
ans =0
def can_go(x,y):
    if 0<=x<n and 0<=y<n and not visited[x][y] and arr[x][y] > t:
        return True
    else:
        return False

def dfs(x,y):
    dxs = [0,0,1,-1]
    dys = [1,-1,0,0]
    visited[x][y] = True
    for dx, dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if can_go(nx,ny):
            dfs(nx,ny)





for t in range(0,rain+1):
    visited = [[ False for _ in range(n)] for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if can_go (i,j):
                visited[i][j] = True
                dfs(i,j)
                cnt+=1
                
    ans =max(ans,cnt)
print(ans)