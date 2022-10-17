n = int(input())
arr = [ i for i in range(1,n+1)]
R =0
pr =0
cnt=0
for L in range(n):
    while R+1<n and pr <n:
        pr+=arr[R]
        R+=1
    if pr == n:
        cnt+=1
    pr-=arr[L]

print(cnt+1)


n = int(input())
arr = [ i for i in range(1,n+1)]
pr = [ 0 for _ in range(n)]
pr[0] = arr[0]
cnt=0
for i in range(1,n):
    pr[i] =pr[i-1]+arr[i]

def get_sum(a,b):
    if a== b:
        return pr[a]
    else:
        return pr[b]-pr[a]

for a in range(n):
    for b in range(a,n):
        if get_sum(a,b) ==n:
            cnt+=1
print(cnt)