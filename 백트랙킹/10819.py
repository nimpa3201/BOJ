n = int(input())
arr =[0]+list(map(int,input().split()))
ans=[]
visited = [0] * (n+1)
maxValue=0

def dfs(num):
    global maxValue
    if num ==n+1:
        tmp=0
        for i in range (len(ans)-1):
            tmp += abs(ans[i]-ans[i-1])
        maxValue=max(maxValue,tmp)
        return
    for i in range(1,n+1):
        if visited[i]:
            continue
        ans.append(arr[i])
        visited[i] =1
        dfs(num+1)
        ans.pop()
        visited[i] =0
dfs(1)
print(maxValue)