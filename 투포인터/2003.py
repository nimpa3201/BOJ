n,m =map(int,input().split())
arr = list(map(int,input().split()))
cnt =0
arr_sum =0
R =0
for L in range(n):
    while R+1 < n and arr_sum  <m :
        arr_sum += arr[R]
        R+=1
    if arr_sum == m :
        cnt+=1
    arr_sum -=arr[L]
print(cnt)

        
