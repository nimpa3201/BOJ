import heapq
n = int(input())
pq = []
score =0
for _ in range(n):
    num =int(input())
    heapq.heappush(pq,num)

while len(pq) !=1 :
    a=heapq.heappop(pq)
    b=heapq.heappop(pq)
    score += a+b
    heapq.heappush(pq,a+b)
print(score)