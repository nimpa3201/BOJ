import sys
sys.setrecursionlimit(2800)
n,m,r = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
order =1
for _ in range(m):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
li = [0 for _ in range(n+1)]

def dfs(n):
    global order
    li[n] = order
    arr[n].sort(reverse= True)
    for i in arr[n]:
        if not visited[i]:  
            visited[i] =1     
            order +=1
            dfs(i)
visited[r] =1
dfs(r)
for i in li[1:]:
    print(i)