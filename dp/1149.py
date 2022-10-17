import sys
INF = sys.maxsize
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[INF for _ in range(3)] for _ in range(n)]
for i in range(3):
    dp[0][i] = arr[0][i]
for i in range(1,n):
    for j in range(3):
        for k in range(3):
            if k!= j:
                dp[i][k] = min(dp[i][k],arr[i][k] +dp[i-1][j])
print(min(dp[-1]))
