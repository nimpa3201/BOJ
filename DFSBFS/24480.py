import sys
sys.setrecursionlimit(10**5)

n,m,r =map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [ 0 for _ in range(n+1)]
li = [ 0 for _ in range(n+1)]
order =1
for _ in range(m):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

def dfs(n):
    global order
    visited[n]=1
    li[n] =order
    order +=1
    arr[n].sort(reverse = False)
    for i in arr[n]:
        if not visited[i]:
            dfs(i)
            
dfs(r)
for i in li[1:]:
    print(i)

    