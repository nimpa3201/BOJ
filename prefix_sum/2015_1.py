import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
tmp =arr[0]
R = 1
cnt=0
for L in range(n):
    while R+1 <= n and tmp <k:
        tmp += arr[R]
        R+=1
    if tmp == k:
        cnt+=1
        print(arr[L],arr[R])
    
    tmp-=arr[L]
print(cnt)
