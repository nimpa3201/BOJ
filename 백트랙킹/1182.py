import sys
sys.setrecursionlimit(10**7)
n,s =map(int,input().split())
arr =list(map(int,input().split()))
ans =[]
output =0
cnt =0
def dfs():
    global cnt
    global output
    if cnt == n:
        if sum(ans) == s:
            output+=1
            return



    else:
        for i in range(len(arr)):
            ans.append(arr[i])
            cnt+=1
            dfs()
            ans.pop()
            cnt+=1

dfs()
print(output)