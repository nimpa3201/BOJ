import sys
import heapq
INF = sys.maxsize
n = int(input())
people  =list(map(int,input().split()))
m = int(input())
graph = [[]for _ in range(n+1)]
num =0
ans =[]
for _ in range(m):
    d,e,l =map(int,input().split())
    graph[d].append((e,l))
    graph[e].append((d,l))
for i in people:
    dist = [INF for _ in range(n+1)]
    dist[i] =0
    pq =[]
    heapq.heappush(pq,(0,i))
    while pq:
        min_dist,min_index = heapq.heappop(pq) 
        if min_dist != dist[min_index]:
            continue
        for target_index,target_dist in graph[min_index]:
            new_dist = min_dist+target_dist
            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    ans.append(dist)
maxim =0
for i in range(1,n+1):
    tmp =min(ans[0][i],ans[1][i],ans[2][i])
    if maxim<tmp:
        maxim =tmp
        num =i
print(num)