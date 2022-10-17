import heapq
import sys
input = sys.stdin.readline
T= int(input())

for _ in range(T):
    ans =0
    n = int(input())
    arr = list(map(int,input().split()))
    pq=[]
    for i in range(n):
        heapq.heappush(pq,arr[i])
    while len(pq) >1 :
        a= heapq.heappop(pq)
        b= heapq.heappop(pq)
        ans +=a+b
        heapq.heappush(pq,a+b)
    print(ans)