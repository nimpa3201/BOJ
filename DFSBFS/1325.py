n,m = map(int,input().split())
graph =[[] for _ in range(n+1)]
visited=set()
count =0
max=0
ans=0
for _ in range(m):
    v1,v2 = tuple(map(int,input().split()))
    graph[v2].append(v1)

def dfs(v):
    global count,ans
    global visited
    visited=set()
    count=0
    visited.add(v)
    for vertex in graph[v]:
        if vertex not in visited:
            visited.add(vertex)
            dfs(vertex)   
            count+=1
    return count
for i in range(1,n+1):
    ans= dfs(i)
    #print(count)
    if ans >=max:
        max=ans
        print(i,end=' ')