n,m = map(int,input().split())
matrix =[list(map(int,input().split())) for _ in range(n)]
dp =[[0 for _ in range(n)] for _ in range(n)]

for i in range (n):   # 초기화하기 각 행에 대해서 구간합을 구하고 , 제외를 행 기준으로 열을 제외하려고함
    dp [i][0]=matrix[i][0]

for i in range(n):
    for j in range(1,n):
        dp[i][j] =dp[i][j-1]+matrix[i][j]
for _ in range(m):
    ans =0  
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    for j in range(x1-1,x2):
        if y1-2 >=0:
            ans += dp[j][y2-1]-dp[j][y1-2]   # 구간에 포함되지 않는 열에 대해 제외 .. 
        else :
            ans += dp[j][y2-1]
    print(ans)