from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q =deque()
count=0

ans=[]
for _ in range(m):
    v1,v2 = tuple(map(int,sys.stdin.readline().split()))
    graph[v2].append(v1)


def push (v) :
    q.append(v)
    visited[v] = True

def bfs():
    global count
    while q:
        v = q.popleft()
        for vertex in graph[v]:
            if not visited[vertex]:
                push(vertex)
                count+=1

for i in range (1,n+1):
    push(i)             # i노드에 대하여 시행
    bfs()
    ans.append(count)   # count 된 거 list에 저장
    count=0             # count 초기화
    visited = [False for _ in range(n+1)]       # visited 초기화

for i in range (len(ans)):  # 최대 count 일때의 i 노드 출력
    if ans[i] == max(ans):
        print(i+1,end=' ')