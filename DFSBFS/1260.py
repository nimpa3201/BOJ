from collections import deque
n,m,r=map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
q= deque()
for _ in range(m):
    v1,v2 = tuple(map(int,input().split()))
    graph[v1].append(v2)
    graph[v1].sort()
    graph[v2].append(v1)
    graph[v2].sort()
def dfs(num):
    for v in graph[num]:
        if not visited[v]:
            visited[v]=1
            print(v,end=' ')
            dfs(v)
visited[r]=1
print(r,end=" ")
dfs(r)
print()                 # DFS


visited = [0 for _ in range(n+1)]
def bfs():
    while q:
        x = q.popleft()
        for next_v in graph[x]:
            if not visited[next_v]:
                print(next_v,end=' ')
                visited[next_v]= 1
                q.append(next_v)


print(r,end=' ')
visited[r] = 1
q.append(r)
bfs()

