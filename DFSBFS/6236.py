import sys
n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
left , right = 0, sum(arr)+1
ans = sys.maxsize

def is_possible(mid):
    cnt =0
    budget = sum(arr) -mid
    k = mid
    for i in arr:
        if i <= k:
            k = k-i
        else:
            budget += i-k
            budget -= mid
            k = mid
            k= k-i
            cnt+=1
    return cnt<=m 



while left <= right :
    mid = (left+right)//2
    if is_possible(mid):
        right =mid-1
        ans =min(ans,mid)
    else:
        left = mid+1
print(ans)