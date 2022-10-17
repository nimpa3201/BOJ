n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
q = list(map(int,input().split()))


def lower_bound(target):
    left = 0                             
    right = n - 1                       
    min_idx = n                          

    while left <= right:                 
        mid = (left + right) // 2        
        if arr[mid] >= target:           
            min_idx = min(min_idx, mid)  
            right = mid - 1             
        else:
            left = mid + 1               
    
    return min_idx             

def upper_bound(target):
    left = 0                             
    right = n - 1                        
    min_idx = n                          

    while left <= right:                
        mid = (left + right) // 2        
        if arr[mid] > target:           
            min_idx = min(min_idx, mid)  
            right = mid - 1              
        else:
            left = mid + 1               
    
    return min_idx                      



for i in q:
    target = i
    print(upper_bound(target)-lower_bound(target),end =' ')
 