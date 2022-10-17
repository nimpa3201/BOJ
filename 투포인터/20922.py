n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = [0]*100001
R = -1
ans =0
for L in range(n):
    while R+1 < n and cnt[arr[R+1]] <m:  
        R+=1
        cnt[arr[R]]+=1
    if  cnt[arr[R]] <= m:
        
        ans = max(ans,R-L+1)   
    cnt[arr[L]]-=1
print(ans)