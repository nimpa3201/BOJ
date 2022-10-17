n = int(input())
m = int(input())
arr= list(map(int,input().split()))
s = set(arr)

cnt=0
for i in arr :
    if m-i in s:
        cnt+=1
print(cnt//2)