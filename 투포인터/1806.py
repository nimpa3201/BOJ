n,s = map(int,input().split())
arr= list(map(int,input().split()))
R =-1
pr=0
ans = n+1
for L in range(n):
    while R+1 < n and pr < s:
        R+=1
        pr+=arr[R]

    if pr >=s :
        ans= min(ans,R-L+1)
    pr-=arr[L]
if ans == n+1:
    ans =-1
print(ans)