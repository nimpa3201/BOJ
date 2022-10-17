import heapq
import sys
INF = sys.maxsize
v,e  = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
dist = [INF for _ in range(v+1)]
for _ in range(e):
    v1,v2,w = map(int,input().split())
    graph[v1].append((v2,w))
dist[k] =0
pq =[]
heapq.heappush(pq,(0,k))
while pq:
    min_dist,min_index =heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue
    for target_index,target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if new_dist < dist[target_index]:
            dist[target_index] = new_dist
            heapq.heappush(pq,(new_dist,target_index))

for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)