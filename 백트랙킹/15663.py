n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans =[]
s =set()
visited =set()
def nPr(num):
    if num == m+1:
        anstuple =tuple(ans)
        s.add(anstuple)
        return
    else:
        for i in range(len(arr)):  
            if ans[-1]!=arr[i]:        
            ans.append(arr[i])
            nPr(num+1)
            ans.pop()
nPr(1)
s= list(s)
s.sort()
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],end=' ')
    print()