n,k = map(int,input().split())
arr =[]
for _ in range(n):
    w,v = map(int,input().split())
    arr.append((w,v))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n):
    for j in range(1,k):
        if dp[i][j-1] <= k :
            dp[i][j] = max(dp[i][j],dp[i][j-1]+arr[i][1])
print(dp)
