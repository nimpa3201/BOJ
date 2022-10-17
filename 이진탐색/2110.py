n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
left =0 
right = max(arr)-min(arr)
ans=0

def is_possible(dist):
    cnt=1
    last_idx =0
    for i in range(1,len(arr)):

        if arr[i] - arr[last_idx] >=dist:
            cnt+=1
            last_idx = i
    return cnt >=m
while left <= right :
    mid = (left+right)//2
    if is_possible(mid):
        left = mid+1
        ans =max(ans,mid)
    else:
        right =mid-1
print(ans)