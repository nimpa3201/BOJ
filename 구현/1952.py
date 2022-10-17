n,m = map(int,input().split())
grid = [ [0 for _ in range(m)] for _ in range(n)]
grid[0][0]=1
dxs, dys = [0,1,0,-1] , [1,0,-1,0]
x,y = 0,0
dir_num = 0
cnt =0
def is_range(x,y):
    return 0<=x<n and 0<=y<m
for i in range(2,n*m+1):
    nx , ny= x+dxs[dir_num], y+dys[dir_num]
    if not is_range(nx,ny) or grid[nx][ny] !=0:
        dir_num = (dir_num+1)%4
        cnt+=1
    
    x,y = x+dxs[dir_num] , y+dys[dir_num]
    grid[x][y] =i
print(cnt)
for i in range(n):
    for j in range(m):
        if grid[i][j] == n*m:
            print(i+1,j+1)