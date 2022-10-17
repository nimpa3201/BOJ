import heapq
n = int(input())
pq =[]
ans =0
s= set()

for _ in range(n):
    p,d = map(int,input().split())
    heapq.heappush(pq,(d,-p))
print(pq)
while pq :
    np,nd =heapq.heappop(pq)
    print(np,nd)
    # for i in range(1,10000+1):
    #     if nd > i:
#     if nd > cnt :
#         ans += np
#         cnt+=1
# print(-ans)
