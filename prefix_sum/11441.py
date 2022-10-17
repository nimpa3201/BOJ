n = int(input())
arr = [0]+list(map(int,input().split()))
m = int(input())
d = [tuple(map(int,input().split())) for _ in range(m)]
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = dp[i-1] + arr[i]

def get_sum(s,e):
    return dp[e]-dp[s]

for i in d:
    print(get_sum(i[0]-1,i[1]))