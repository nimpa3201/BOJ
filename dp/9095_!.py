T= int(input())

def sol(num):
    dp = [0 for _ in range(n)]
    if num >3:
        
        dp[0] =1
        dp[1]=2
        dp[2]=4
 
       
        for i in range(3,num):
            dp[i] =dp[i-1]+dp[i-2]+dp[i-3]
        return dp[num-1]
    else:
        if num ==1:
            return 1
        if num ==2:
            return 2
        if num ==3:
            return 4

for _ in range(T):
    n = int(input())
    print(sol(n))