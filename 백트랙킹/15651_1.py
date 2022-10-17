

n,m =map(int,input().split())
ans =[]
def backtrack(num):
    if num == m+1:
        for i in ans:
            print(i , end=' ')
        print()
        return 
    else:
        for i in range(1,n+1):
            ans.append(i)
            backtrack(num+1)
            ans.pop()
backtrack(1)
        