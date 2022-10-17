n,m = map(int,input().split())
matrix =[list(map(int,input().split())) for _ in range(n)]

    

def sumMatrix(x1,y1,x2,y2):
    ans =0
    for col in range(x1-1,x2):
        for row in range(y1-1,y2):
            ans +=matrix[col][row]
    return ans
for _ in range(m):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    print(sumMatrix(x1,y1,x2,y2))
    