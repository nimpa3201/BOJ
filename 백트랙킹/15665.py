n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans =[]
s =set()
def dfs(num):
    if num ==m+1:
        t = tuple(ans)
        s.add(t)
        return

    else:
        for i in range(len(arr)):
            ans.append(arr[i])
            dfs(num+1)
            ans.pop()
dfs(1)
s= list(s)
s.sort()
for i in s:
    print(*i)