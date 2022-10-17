import sys
sys.setrecursionlimit(10000)
def dfs(x,y):
    dxs = [0,0,-1,1,-1,1,-1,1]
    dys = [1,-1,0,0,-1,-1,1,1]
    arr[x][y] =0
    for dx, dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if can_go(nx,ny):
            dfs(nx,ny)
    

def can_go(x,y):
    if is_range(x,y)  and arr[x][y] ==1:
        return True
    else:
        return False

def is_range(x,y):
    return 0<=x<h and 0<=y<w






while True:
    w, h = map(int,input().split())
    count=0
    if w == 0 and h ==0 :
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    print(arr)
    for i in range(h):
        for j in range(w):
            if can_go(i,j):
                dfs(i,j)
                count+=1
    print(count)