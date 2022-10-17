n,m = map(int,input().split())
ans =[]
def nPr(num,pvt):
    if num == m+1:
        for i in ans:
            print(i,end =' ')
        print()

    else:
        for i in range(pvt,n+1):
            ans.append(i)
            nPr(num+1,i+1)
            ans.pop()
nPr(1,1)