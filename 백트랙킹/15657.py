n,m =map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()
ans =[]
def nPr(num,pivot):
    if num == m+1:
        for i in ans:
            print(i,end=' ')
        print()
        return
    else:
        for i in range(pivot,n):
            ans.append(arr[i])
            nPr(num+1,i)
            ans.pop()
nPr(1,0)