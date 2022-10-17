import sys
input =  sys.stdin.readline
sys.setrecursionlimit(250001)
n,m = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
ans =0
li =[]
count =0

def dfs(x,y):
    global count 
    if 0<=x<n and 0<=y<m and not visited[x][y] and grid[x][y] ==1:
        count+=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    else:
        return False
    
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True : 
            count=1
            visited[i][j]= True    
            dfs(i,j)
            li.append(count)
a= len(li) 
print(a)
if a!=0:
    print(max(li))
else:
    print(0)
