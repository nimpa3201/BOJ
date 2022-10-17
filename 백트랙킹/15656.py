n,m =map(int,input().split())
arr= list(map(int,input().split()))
ans =[]
arr.sort()
def nPr(num):
    if num == m+1:
        for i in ans:
            print(i,end=' ')
        print()
        return
    else:
        for i in arr:
            ans.append(i)
            nPr(num+1)
            ans.pop()
nPr(1)
