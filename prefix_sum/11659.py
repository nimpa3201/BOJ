import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[1]= arr[0]
for i in range(2,n+1):
    dp[i] =dp[i-1]+arr[i-1]
def get_sum(s,e):
    return dp[e]-dp[s-1]
for _ in range(m):
    s,e = map(int,input().split())
    print(get_sum(s,e))