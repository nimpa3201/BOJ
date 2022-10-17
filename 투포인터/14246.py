n =int(input())
arr= list(map(int,input().split()))
k = int(input())
R =0
pr=0
cnt=0
for L in range(n):
    while R+1 <n :
        R+=1
        pr +=arr[R]
    if pr >= k :
        cnt+=1
    pr-=arr[L]
print(cnt)