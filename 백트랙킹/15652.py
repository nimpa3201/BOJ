n,m = map(int,input().split())
ans =[]
def npr(num):
    if num ==m+1:
        for i in ans:
            print(i ,end = ' ')
        print()
        return
    else:
        for i in range(1,n+1):
            if len(ans) ==0 or ans[-1]<=i:
                ans.append(i)
                npr(num+1)
                ans.pop()
npr(1)
