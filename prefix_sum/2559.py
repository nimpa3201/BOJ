import sys
n,k = map(int,input().split())
arr = [0]+ list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
result = -sys.maxsize
for i in range(1,n+1):
    dp[i] = dp[i-1]+arr[i]

def get_sum(s,e):
    return dp[s]-dp[e]

for i in range(0,n-k+1):
    ans =get_sum(i+k,i)
    if ans > result :
        result =ans
print(result) 