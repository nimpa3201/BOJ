import heapq
import sys
INF = sys.maxsize
n,m,x =map(int,input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,input().split())
    graph1[e].append((s,t))
    graph2[s].append((e,t))

def dijkstra(graph,start):
    dist = [INF for _ in range(n+1)]
    dist[start] =0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq :
        min_dist,min_index = heapq.heappop(pq)

        if min_dist != dist[min_index]:
            continue
        for target_index,target_dist in graph[min_index]:
            new_dist = min_dist+target_dist
            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    return dist
vill_to_x=dijkstra(graph1,x)
x_to_vill =dijkstra(graph2,x)
ans =0
for i in range(1,n+1):
    ans =max(ans,vill_to_x[i]+x_to_vill[i])
print(ans)
