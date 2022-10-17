from collections import deque
q =deque()
n,m,r = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
visited = [0 for _ in range(n+1)]
def bfs():
    order=1
    while q:
        a= q.popleft()
        for i in sorted(arr[a]):
            if  not visited[i]:
                order+=1
                visited[i] =order
                q.append(i)

q.append(r)
visited[r] = 1
bfs()
for i in visited[1:]:
    print(i)