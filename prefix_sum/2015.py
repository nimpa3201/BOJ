import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
pr =[0 for _ in range(n)]
cnt=0
pr[0] = arr[0]
for i in range(1,n):
    pr[i] =pr[i-1]+arr[i]

def get_sum (s,e):
    return pr[e]-pr[s]

for i in range(0,n):
    for j in range(i,n):
        if i == j:
            key= pr[i]
        else:
            key = get_sum(i,j)

        if key == k:
            cnt+=1
print(cnt)