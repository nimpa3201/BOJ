n,m = map(int,input().split())
ans =[]
def ncm(num):
    if num ==m+1:
        for i in ans:
            print(i,end =' ')
        print()
    else :
        for i in range(1,n+1):
            ans.append(i)
            ncm(num+1)
            ans.pop()
ncm(1)