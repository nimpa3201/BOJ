n,m =map(int,input().split())
ans = []
def nPr (num):
    if num == m+1:
        for i in ans:
            print(i,end =' ')
        print()
        return
    else:
        for i in range(1,n+1):
            if len(ans) ==0 or i not in ans:
                ans.append(i)
                nPr(num+1)
                ans.pop()
nPr(1)