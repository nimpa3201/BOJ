import sys
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
L,R = 0,n-1
li =[]
mini = sys.maxsize
while L < R :
    v =arr[R]+arr[L]
    if mini > abs(v) :
        mini =abs(v)
        li.append((L,R))
    if v<0:
        L +=1
    if v> 0:
        R-=1
    if v==0:
        break
print(arr[li[-1][0]],arr[li[-1][1]])