n = int(input())
arr = list(map(int,input().split()))
budget = int(input())
left , right = 0, max(arr)
ans =0
def is_possible(mid):
    cal = []
    for i in range(len(arr)):
        if arr[i] > mid :
            cal.append(mid)
        else:
            cal.append(arr[i])
    return sum(cal) <=budget
   
while left <= right :
    mid = (left+right)//2
    if  is_possible(mid):
        left = mid+1
        ans = max(ans,mid)
    else:
        right = mid-1
print(ans)