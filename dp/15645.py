import sys
n =int(input())
INF = sys.maxsize
arr = [ list(map(int,input().split())) for _ in range(n)]
max_dp = [[0 for _ in range(3)] for _ in range(n)]
min_dp = [[INF for _ in range(3)] for _ in range(n)]

for i in range(3):
    max_dp[0][i] =arr[0][i]
    min_dp[0][i] = arr[0][i]
for i in range(1,n):
        max_dp[i][0] = max(max_dp[i-1][0],max_dp[i-1][1])+arr[i][0]
        min_dp[i][0] = min(min_dp[i-1][0],min_dp[i-1][1])+arr[i][0]
        max_dp[i][2] = max(max_dp[i-1][2],max_dp[i-1][1])+arr[i][2]
        min_dp[i][2] = min(min_dp[i-1][2],min_dp[i-1][1])+arr[i][2]
        max_dp[i][1] = max(max_dp[i-1][0],max_dp[i-1][2],max_dp[i-1][1])+arr[i][1]
        min_dp[i][1] = min(min_dp[i-1][0],min_dp[i-1][2],min_dp[i-1][1])+arr[i][1]
print(max(max_dp[n-1]),min(min_dp[n-1]))

