n = int(input()) # 노드개수
m = int(input()) # m 간선 개수
graph =[[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt=0
for _ in range(m):
    v1,v2 = tuple(map(int,input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(num):
    global cnt
    for v in graph[num]:
        if not visited[v] :
            visited[v]=1 
            cnt+=1        
            dfs(v)

visited[1]=1
dfs(1)     

print(cnt)