n,m  = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right =max(arr)
ans =0

def is_possible(d):
    a=0
    for i in arr:
        if i > d :
            a+= i-d
    return a>=m

while left <= right:
    mid = (left+right)//2

    if is_possible(mid):
        left = mid+1
        ans= max(ans,mid)
    else:
        right = mid-1

print(ans)