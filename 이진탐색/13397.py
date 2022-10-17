n,m = map(int,input().split())
arr = list(map(int,input().split()))
left =0
right = max(arr)-min(arr)
ans = right +1


def is_possible(mid):
    cnt =1
    low = arr[0]
    high = arr[0]
    for i in arr:
        if i <low :
            low =i
        if i > high:
            high = i
        if high - low > mid:
            cnt+=1
            low =i
            high =i

    return cnt <=m



while left <= right:               
    mid = (left + right) // 2      
    if is_possible(mid):          
        right = mid - 1            
        ans = min(ans, mid)       
    else:                               
        left = mid + 1             
print(ans)