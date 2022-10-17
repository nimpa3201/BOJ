import sys
n =int(input())
arr = list(map(int,input().split()))
arr.sort()
L ,R = 0, n-1
ans = sys.maxsize
li =[]
while L < R :
    v = arr[R] + arr[L]
    if ans >= abs(v):
        ans = abs(v)
        li.append([arr[R],arr[L]])
    if v > 0:  
        R-=1
    if v< 0:
        L+=1
    if v ==0:
        break
li[-1].sort()
print(li[-1][0],li[-1][1])