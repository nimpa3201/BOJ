n = int(input())
a= set(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split()))
for i in arr:
    if i in a:
        print(1)
    else:
        print(0)