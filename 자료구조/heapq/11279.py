import heapq
import sys
n = int( sys.stdin.readline())
pq =[]

for _ in range(n):
    m = int( sys.stdin.readline())

    if m ==0:
        if len(pq)==0:
            print(0)
        else:
            a=heapq.heappop(pq)
            print(-a)
    else:
        heapq.heappush(pq,-m)
