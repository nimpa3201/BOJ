import sys
import heapq
T = int(input())
INF =sys.maxsize
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    dist = [ INF for _ in range(n+1)]
    dist[c] =0
    pq =[]
    heapq.heappush(pq,(0,c))
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    while pq:
        min_dist,min_idx = heapq.heappop(pq)
        if dist[min_idx] !=min_dist:
            continue
        for target_index,target_dist in graph[min_idx]:
            new_dist = min_dist+target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq,(new_dist,target_index))
    cnt=0
    ans =0
    for i in dist[1:]:
        if i != INF:
            cnt+=1
            ans = max(ans,i)
    print(cnt,ans)

        
            


