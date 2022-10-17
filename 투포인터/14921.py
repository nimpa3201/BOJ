import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
L,R =0,n-1
ans =arr[L]+arr[R]
while L < R :
    v = arr[L]+arr[R]
    if abs(ans) > abs(v):
        ans =v
    if v < 0 :
        L+=1
    else:        
        R-=1
print(ans)