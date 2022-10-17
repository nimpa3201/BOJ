from collections import deque
n = int(input())
a ,b = map(int,input().split())
m = int(input())
q =deque()
li =[[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt=0
for _  in range(m):
    x,y = tuple(map(int,input().split()))
    li[x].append(y)
    li[y].append(x)

def bfs():
    q.append(a)  
    while q:
        x = q.popleft()
        for next_v in li[x]:
            if not visited[next_v]:
                q.append(next_v)
                visited[next_v]=visited[x]+1

 
bfs()        
print(visited[b] if visited[b] >0 else -1)