import heapq

pq =[]
bin =[]
n = int(input())
arr= []
for _ in range(n):
    arr.append(int(input()))
for i in range (len(arr)):
    heapq.heappush(pq,arr[i])   
    for j in range(i+1):
        a=heapq.heappop(pq)
        bin.append(a)
        if (i//2) == j :
            print(a)
    for k in bin:
        heapq.heappush(pq,k)
    bin =[]
            