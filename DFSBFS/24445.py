from collections import deque
n,m,k = map(int,input().split())
arr = [[]for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
visited =[ 0 for _ in range(n+1)]
q =deque()
def bfs():
    order =1
    while q:
        x= q.popleft()
        for next_v in sorted(arr[x],reverse=True):
            if not visited[next_v]:
                order +=1
                visited[next_v] = order
                q.append(next_v)
q.append(k)
visited[k]=1               
bfs()
for i in visited[1:]:
    print(i)