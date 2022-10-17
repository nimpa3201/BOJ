import heapq
import sys
INF = sys.maxsize
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    v1,v2,w = map(int,input().split())
    graph[v1].append((v2,w))
    graph[v2].append((v1,w))
con1,con2 = map(int,input().split())
def dijkstra(star,end):
    pq =[]
    dist = [INF for _ in range(n+1)]
    dist[star] =0
    heapq.heappush(pq,(0,star))
    while pq:
        min_dist , min_index = heapq.heappop(pq)   
        if min_dist != dist[min_index]:
            continue
        for new_index,new_dist in graph[min_index]:
            if dist[new_index] > min_dist + new_dist:
                dist[new_index] = min_dist+ new_dist
                heapq.heappush(pq,(min_dist+new_dist,new_index))
    return dist[end]
ans = min(dijkstra(1,con1)+dijkstra(con1,con2)+dijkstra(con2,n),dijkstra(1,con2)+dijkstra(con2,con1)+dijkstra(con1,n))
if dijkstra(1,con1) == INF or  dijkstra(con1,con2) == INF or  dijkstra(con2,n) ==INF or dijkstra(1,con2) == INF or dijkstra(con1,n) == INF:
    print(-1)
else:
    print(ans)