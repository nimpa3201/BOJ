n = int(input())
# dp = [0] *(46)
# dp[0] =0
# dp[1] =1
# for i in range(2,n+1):
#     dp[i] = dp[i-1]+dp[i-2]
# print(dp[n])
def pibo(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    return pibo(n-1)+pibo(n-2)
print(pibo(n))