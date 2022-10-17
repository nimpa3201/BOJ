import sys
input =sys.stdin.readline
n = int(input())
arr= [int(input()) for _ in range(n)]

cnt=0
tmp = arr[-1]
for i in arr[::-1] :
    if i> tmp:
        tmp =i
        cnt+=1 
    
print(cnt+1)