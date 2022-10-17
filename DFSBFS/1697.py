from collections import deque
n ,m = map(int,input().split())
visited = [0 for _ in range(100001)]
q =deque()

def bfs():
    q.append(n)
    while q:
        x= q.popleft()
        if x == m:
            print(visited[x])
            break
        move = [x-1, x+1, 2*x]
        for i in move:
            if  is_range(i) and not visited[i] : 
                q.append(i)
                visited[i] = visited[x]+1  
def is_range(x):
    return 0<=x <=100000
bfs()