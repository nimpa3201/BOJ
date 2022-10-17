import sys
import heapq
INF = sys.maxsize
n =int(input())
m =int(input())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
k,d = map(int,input().split())
dist[k]=0
pq =[]
heapq.heappush(pq,(0,k))
while pq:
    min_dist,min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue
    for target_index,target_dist  in graph[min_index]:
        new_dist = dist[min_index]+target_dist
        if new_dist < dist[target_index]:
            dist[target_index] = new_dist
            heapq.heappush(pq,(new_dist,target_index))
print(dist[d])